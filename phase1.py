from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton

from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty

from materials import word_to_letter
import speech_recognition as sr
#from sound_recorder import rec
from jniusrecord import android_record
import random
import numpy as np
import os

from tinydb import TinyDB, Query
from materials import FILIPINO_ALPHABETS, TOTAL_ALPHABETS


class IntroToAlphabets(Screen):

    def __init__(self, **kwargs):
        super(IntroToAlphabets, self).__init__(**kwargs)
        self.abctable = self.ids.abc
        self.sound = None
        self.button = None
        
        for letter in FILIPINO_ALPHABETS:
            self.button = MDRaisedButton(text=letter+letter.lower(),font_size='30sp', size_hint=(1,None), font_name='NotoSerif-Regular.ttf')
            self.button.bind(on_press=self.say_the_letter)
            self.abctable.add_widget(self.button)
        
    
    def say_the_letter(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            if instance.text == "NGng":
                self.sound = SoundLoader.load(f'src/phase1/alphabets/NG.ogg')
            elif instance.text == "Ññ":
                self.sound = SoundLoader.load(f'src/phase1/alphabets/ENYE.ogg')
            else:
                self.sound = SoundLoader.load(f'src/phase1/alphabets/{instance.text[0]}.ogg')
            self.sound.play()


class PhaseOneTest(Screen):#IntroToAlphabets
    the_alphabet = ObjectProperty(None)
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
        super(PhaseOneTest, self).__init__(**kw)
        self.the_alphabet.final_pos = self.the_alphabet.pos

  
    def show_letter(self):
        zzz = len(self.corrected)/56
        self.progress_bar.value = zzz * 100
        if len(self.corrected) != 56:
            self.current_answer = random.choice(TOTAL_ALPHABETS)
            while self.current_answer in self.corrected:
                self.current_answer = random.choice(TOTAL_ALPHABETS)

            self.the_alphabet.final_pos = self.the_alphabet.pos
            x,y = self.the_alphabet.final_pos
            self.the_alphabet.pos = (x, y+self.height)

            self.the_alphabet.children[0].text = f"{self.current_answer}"
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.the_alphabet)
            self.corrected.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL Letters ALREADY ANSWERED')

        self.speaker.theme_icon_color = "Primary"
        self.next_button.disabled = True

    def start_show_letter(self, dt):

        if len(self.corrected) != 56:
            self.current_answer = random.choice(TOTAL_ALPHABETS)
            while self.current_answer in self.corrected:
                self.current_answer = random.choice(TOTAL_ALPHABETS)

            self.the_alphabet.final_pos = self.the_alphabet.pos
            x,y = self.the_alphabet.final_pos
            self.the_alphabet.pos = (x, y+self.height)
            
            self.the_alphabet.children[0].text = f"{self.current_answer}"
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.the_alphabet)
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
          
        verify = self.check_answer(f'answers/phase1/{self.answer_file}')
        if verify: #IF CORRECT ANSWER
            self.speaker.theme_icon_color="Custom"
            self.speaker.icon_color = (0,1,0.3,1)
            self.next_button.disabled = False
        else: #IF WRONG ANSWER
            self.speaker.theme_icon_color="Custom"
            self.speaker.icon_color = (0.3,0,0,1)
            self.next_button.disabled = True

        

    def answer(self):
        if self.current_answer.isupper():
            self.answer_file = 'big' + '-' + self.current_answer + '.amr'
        else:
            self.answer_file = 'small' + '-' + self.current_answer + '.amr'
        duration = 4
        freq = 44100
        #record = rec(f'answers/phase1/{self.answer_file}', duration, freq)
        record = android_record(f'answers/phase1/{self.answer_file}')
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
                understand = word_to_letter(self.current_answer, result)
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
        if self.current_answer.isupper():
            self.answer_file = 'big' + '-' + self.current_answer + '.amr'
        else:
            self.answer_file = 'small' + '-' + self.current_answer + '.amr'

        if self.answer_file in self.tries:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'answers/phase1/{self.answer_file}')
            self.sound.play()
        else:
            print('answer first!')



class TheAlphabet(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)

    

