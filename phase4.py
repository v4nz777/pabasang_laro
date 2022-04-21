from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty
from materials import CVCE,CVCA, CVCE, CVCI, CVCO, CVCU, CVC_QUIZ
import random
from kivy.clock import Clock

import speech_recognition as sr
#from sound_recorder import rec
from jniusrecord import android_record

from tinydb import TinyDB, Query
from materials import understand_tlw


class Cvc(Screen):
    pass

class VowelA(Screen):
    def __init__(self, **kw):
        super(VowelA, self).__init__(**kw)
        self._list = self.ids.cvc_a
        self.say_word = None
        for i in CVCA:
            if len(i) == 3:
                self.btn = MDFillRoundFlatButton(
                    text=i, 
                    font_size=50, 
                    padding=(30,8,30,8),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
                self.btn.bind(on_release=self.callbck)
                self._list.add_widget(self.btn)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/tts/a/{instance.text}_slow.ogg')
            self.say_word.play()
    
class VowelE(Screen):
    def __init__(self, **kw):
        super(VowelE, self).__init__(**kw)
        self._list = self.ids.cvc_e
        self.say_word = None
        for i in CVCE:
            if len(i) == 3:
                self.btn = MDFillRoundFlatButton(
                    text=i, 
                    font_size=50, 
                    padding=(30,8,30,8),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
                self.btn.bind(on_release=self.callbck)
                self._list.add_widget(self.btn)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/tts/e/{instance.text}_slow.ogg')
            self.say_word.play()

class VowelI(Screen):
    def __init__(self, **kw):
        super(VowelI, self).__init__(**kw)
        self._list = self.ids.cvc_i
        self.say_word = None
        for i in CVCI:
            if len(i) == 3:
                self.btn = MDFillRoundFlatButton(
                    text=i, 
                    font_size=50, 
                    padding=(30,8,30,8),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
                self.btn.bind(on_release=self.callbck)
                self._list.add_widget(self.btn)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/tts/i/{instance.text}_slow.ogg')
            self.say_word.play()

class VowelO(Screen):
    def __init__(self, **kw):
        super(VowelO, self).__init__(**kw)
        self._list = self.ids.cvc_o
        self.say_word = None
        for i in CVCO:
            if len(i) == 3:
                self.btn = MDFillRoundFlatButton(
                    text=i, 
                    font_size=50, 
                    padding=(30,8,30,8),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
                self.btn.bind(on_release=self.callbck)
                self._list.add_widget(self.btn)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/tts/o/{instance.text}_slow.ogg')
            self.say_word.play()

class VowelU(Screen):
    def __init__(self, **kw):
        super(VowelU, self).__init__(**kw)
        self._list = self.ids.cvc_u
        self.say_word = None
        for i in CVCU:
            if len(i) == 3:
                self.btn = MDFillRoundFlatButton(
                    text=i, 
                    font_size=50, 
                    padding=(30,8,30,8),
                    pos_hint={"center_x": .5, "center_y": .5},
                )
                self.btn.bind(on_release=self.callbck)
                self._list.add_widget(self.btn)
            
    def callbck(self,instance):
        if instance.text:
            if self.say_word:
                self.say_word.stop()
            self.say_word = SoundLoader.load(f'src/phase4/tts/u/{instance.text}_slow.ogg')
            self.say_word.play()


###################################### CVC GAME ############################################
class CvcQuiz(MDScreen):
    word_box = ObjectProperty(None)
    shown = []
    current_answer = ""
    current_answer = StringProperty("")
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
        zzz = len(self.shown)/50
        self.progress_bar.value = zzz * 100
        if len(self.shown) != 50:
            self.current_answer = random.choice(CVC_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(CVC_QUIZ)

            self.word_box.final_pos = self.word_box.pos
            x,y = self.word_box.final_pos
            self.word_box.pos = (x, y+self.height)

            self.word_box.children[0].source = f"imgs/word_blocks/{self.current_answer}.png"
            anim1 = Animation(y=y, size=(80, 80), t='out_bounce')
            anim1.start(self.word_box)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL 50 ALREADY ANSWERED')

        self.speaker.theme_icon_color = "Primary"
        self.next_button.disabled = True

    def start_show_word(self, dt):
        if len(self.shown) != 50:
            self.current_answer = random.choice(CVC_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(CVC_QUIZ)
            
            self.word_box.final_pos = self.word_box.pos
            x,y = self.word_box.final_pos
            self.word_box.pos = (x, y+self.height)

            self.word_box.children[0].source = f"imgs/word_blocks/{self.current_answer}.png"
            anim1 = Animation(y=y, size=(80, 80), t='out_bounce')
            anim1.start(self.word_box)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL 50 ALREADY ANSWERED')
        self.next_button.disabled = True

    def on_enter(self):
        Clock.schedule_once(self.start_show_word)

    def validate(self):
        answer = self.answer()
        while not answer:
            self.microphone.disabled = True
            self.microphone.theme_icon_color="Custom"
            self.microphone.icon_color = (0,1,0.3,1)
          
        verify = self.check_answer(f'answers/phase4/{self.answer_file}')
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
        #record = rec(f'answers/phase4/{self.answer_file}', duration, freq)
        record = android_record(f'answers/phase4/{self.answer_file}')

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
            self.sound = SoundLoader.load(f'answers/phase4/{self.answer_file}')
            self.sound.play()
        else:
            print('answer first!')
         
class WordBox(Scatter):
    word = StringProperty("")
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)

    
    