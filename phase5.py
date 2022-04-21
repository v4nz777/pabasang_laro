from kivymd.uix.screen import MDScreen
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty
from materials import CVC2_QUIZ
import random
from kivy.clock import Clock

import speech_recognition as sr
#from sound_recorder import rec
from jniusrecord import android_record
from tinydb import TinyDB, Query
from materials import understand_tlw

class CVCandE(MDScreen):
    _m = ObjectProperty(None)
    _l = ObjectProperty(None)
    _s = ObjectProperty(None)
    _b = ObjectProperty(None)
    _empty = ObjectProperty(None)

class Empty(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty("")

class Letter(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty("")
    sound = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_touch_up(self, touch):        
        #left side
        if self.collide_widget(self.parent.parent.parent._empty):
            self.parent.parent.parent._empty.children[0].source = f"imgs/letter_blocks/{self.letter}.png"
            # = f"imgs/letter_blocks/{self.letter}.png"
            print(f"{self.letter}ake")
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase5/{self.letter}ake.ogg')
            self.sound.play()
        self.pos = self.initial_pos

        

        if touch in self._touches and touch.grab_state:
            touch.ungrab(self)
            del self._last_touch_pos[touch]
            self._touches.remove(touch)


    ############## QUIZ #########################################################################
 
class CvcQuiz2(MDScreen):
    word_outline = ObjectProperty(None)
    current_answer = StringProperty("")
    shown = ListProperty([])
    showed = ListProperty([])
    tries = ListProperty([])
    corrected = ListProperty([])

    sound = ObjectProperty(None)
    
    progress_bar = ObjectProperty(None)
    microphone = ObjectProperty(None)
    speaker = ObjectProperty(None)
    next_button = ObjectProperty(None)
    toolbar = ObjectProperty(None)

    def show_word(self):
        zzz = len(self.shown)/10
        self.progress_bar.value = zzz * 100
        if len(self.shown) != 10:
            self.current_answer = random.choice(CVC2_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(CVC2_QUIZ)

            self.word_outline.final_pos = self.word_outline.pos
            x,y = self.word_outline.final_pos
            self.word_outline.pos = (x, y+self.height)
            
            self.word_outline.children[0].source = f"imgs/cvcplus/{self.current_answer}.png"
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.word_outline)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL 10 ALREADY ANSWERED')

        self.speaker.theme_icon_color = "Primary"
        self.next_button.disabled = True


    def start_show_word(self, dt):
        if len(self.shown) != 10:
            self.current_answer = random.choice(CVC2_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(CVC2_QUIZ)

            self.word_outline.final_pos = self.word_outline.pos
            x,y = self.word_outline.final_pos
            self.word_outline.pos = (x, y+self.height)
            
            self.word_outline.children[0].source = f"imgs/cvcplus/{self.current_answer}.png"
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.word_outline)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL 10 ALREADY ANSWERED')
    

    def on_enter(self):
        Clock.schedule_once(self.start_show_word)

    def validate(self):
        answer = self.answer()
        while not answer:
            self.microphone.disabled = True
            self.microphone.theme_icon_color="Custom"
            self.microphone.icon_color = (0,1,0.3,1)
          
        verify = self.check_answer(f'answers/phase5/{self.answer_file}')
        if verify: #IF CORRECT ANSWER
            self.speaker.theme_icon_color="Custom"
            self.speaker.icon_color = (0,1,0.3,1)
            self.next_button.disabled = False
        else: #IF WRONG ANSWER
            self.speaker.theme_icon_color="Custom"
            self.speaker.icon_color = (0.3,0,0,1)
            self.next_button.disabled = True


    def answer(self):
        self.answer_file = self.current_answer + '.amr'
        duration = 4
        freq = 44100
        #record = rec(f'answers/phase5/{self.answer_file}', duration, freq)
        record = android_record(f'answers/phase5/{self.answer_file}')
        self.tries.append(self.answer_file)
        return True

    def check_answer(self, file):
        r = sr.Recognizer()
        with sr.AudioFile(file) as source:
            audio = r.listen(source)
            try:
                #FOR OFFLINE r.recognize_sphinx(audio)
                #FOR ONLINE r.recognize_google(audio)
                result = r.recognize_google(audio, language= "en-PH")
                print(result)
                understand = understand_tlw(self.current_answer, result)
                if understand:
                    return True

            except:
                print('did not understand')
                db = TinyDB('db.json')
                Mode = Query()
                game_settings = db.search(Mode.name == 'game_settings')
                if game_settings[0]['offline_mode']:
                    print('OFFLINE MODE DETECTED')
                    return True
                return False

    def listen_answer(self):
        self.answer_file = self.current_answer + '.amr'

        if self.answer_file in self.tries:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'answers/phase5/{self.answer_file}')
            self.sound.play()
        else:
            print('answer first!')   

class WordOutline(Scatter):
    word = StringProperty("")
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)


