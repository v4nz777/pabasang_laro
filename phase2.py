from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton

from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty

from materials import word_to_phonetics
import speech_recognition as sr
#from sound_recorder import rec
from jniusrecord import android_record



import random

from tinydb import TinyDB, Query
from materials import FILIPINO_ALPHABETS

from materials import lowercase as fil_lowercase
from materials import understand_tlw

class Phoenetics(Screen):
    def __init__(self, **kwargs):
        super(Phoenetics, self).__init__(**kwargs)

        self.phoenetics = self.ids.phoenetics
        self.sound = None
        self.button = None

        for letter in FILIPINO_ALPHABETS:
            self.button = MDRectangleFlatButton(text=letter.lower(),font_size='30sp', size_hint_y=None, font_name='NotoSerif-Regular.ttf')
            self.button.bind(on_press=self.letter_sound)
            self.phoenetics.add_widget(self.button)
        
    def letter_sound(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            if instance.text == "ng":
                self.sound = SoundLoader.load(f'src/phase2/letter_sounds/NG.ogg')
            elif instance.text == "ñ":
                self.sound = SoundLoader.load(f'src/phase2/letter_sounds/enye.ogg')
            else:
                text_filename = instance.text[0].upper()
                self.sound = SoundLoader.load(f'src/phase2/letter_sounds/{text_filename}.ogg')
            self.sound.play()


class PhaseTwoTest(Screen):
    the_letter = ObjectProperty(None)
    progress_bar = ObjectProperty(None)
    microphone = ObjectProperty(None)
    speaker = ObjectProperty(None)
    next_button = ObjectProperty(None)
    toolbar = ObjectProperty(None)
    sound = None

    tries = []
    corrected = [] #['m', 'w']
    current_answer = ""
    answer_file = ""

    def __init__(self, **kw):
        super(PhaseTwoTest, self).__init__(**kw)
        self.the_letter.final_pos = self.the_letter.pos
    
    def show_letter(self):
        zzz = len(self.corrected)/28
        self.progress_bar.value = zzz * 100
        if len(self.corrected) != 28:
            self.current_answer = random.choice(fil_lowercase)
            while self.current_answer in self.corrected:
                self.current_answer = random.choice(fil_lowercase)

            self.the_letter.final_pos = self.the_letter.pos
            x,y = self.the_letter.final_pos
            self.the_letter.pos = (x, y+self.height)

            self.the_letter.children[0].text = f"{self.current_answer}"
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.the_letter)
            self.corrected.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL Letters ALREADY ANSWERED')
        self.speaker.theme_icon_color = "Primary"
        self.next_button.disabled = True

    def start_show_letter(self, dt):

        if len(self.corrected) != 28:
            self.current_answer = random.choice(fil_lowercase)
            while self.current_answer in self.corrected:
                self.current_answer = random.choice(fil_lowercase)

            self.the_letter.final_pos = self.the_letter.pos
            x,y = self.the_letter.final_pos
            self.the_letter.pos = (x, y+self.height)

            self.the_letter.children[0].text = f"{self.current_answer}"
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.the_letter)
            self.corrected.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL Letters ALREADY ANSWERED')
        self.speaker.theme_icon_color = "Primary"
        self.next_button.disabled = True

    def on_enter(self):
        Clock.schedule_once(self.start_show_letter)

    def validate(self):
        answer = self.answer()
        while not answer:
            self.microphone.disabled = True
            self.microphone.theme_icon_color="Custom"
            self.microphone.icon_color = (0,1,0.3,1)
          
        verify = self.check_answer(f'answers/phase2/{self.answer_file}')
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
        #record = rec(f'answers/phase2/{self.answer_file}', duration, freq)
        record = android_record(f'answers/phase2/{self.answer_file}')
        self.tries.append(self.answer_file)
        return True
    
    def check_answer(self, file):
        r = sr.Recognizer()
        with sr.AudioFile(file) as source:
            audio = r.listen(source)
            try:
                #FOR OFFLINE r.recognize_sphinx(audio)
                #FOR ONLINE r.recognize_google(audio)
                result = r.recognize_google(audio, language="en-PH")
                print(result)
                understand = word_to_phonetics(self.current_answer, result)
                if understand:
                    return True
                elif understand_tlw(self.current_answer, result):
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
            self.sound = SoundLoader.load(f'answers/phase2/{self.answer_file}')
            self.sound.play()
        else:
            print('answer first!')



class TheLetter(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)