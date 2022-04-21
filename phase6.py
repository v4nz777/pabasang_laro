from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFillRoundFlatButton, MDRaisedButton
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty
from materials import DIPTHONGS, DIPTHONGS_EX, DIGRAPHS, DIGRAPHS_EX,  CONSONANTBLENDS, CONSONANTBLENDS_EX, DIP_DIG_CON_QUIZ
import random
from kivy.clock import Clock

import speech_recognition as sr
#from sound_recorder import rec
from jniusrecord import android_record
from tinydb import TinyDB, Query
from materials import understand_tlw

class Sample(Scatter):
    sound = ObjectProperty(None)
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    subject = StringProperty("")

    def __init__(self, **kwargs):
        super(Sample, self).__init__(**kwargs)
        self.add_widget(MDFillRoundFlatButton())
        self.size_hint = (None, None)
        self.size = self.children[0].size

    def listen(self, instance):
        
        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(f'src/phase6/{instance.text}.ogg')
        self.sound.play()
        


class Phase6Main(MDScreen):
    dipthongs_samp: ObjectProperty(None)
    digraphs_samp: ObjectProperty(None)
    consblends_samp: ObjectProperty(None)
    
    def __init__(self, **kw):
        super(Phase6Main, self).__init__(**kw)


        for dipt in DIPTHONGS:
            self.scat = Sample()
            self.scat.children[0].text = dipt
            self.scat.children[0].bind(on_release = self.scat.listen)
            self.dipthongs_samp.add_widget(self.scat)

        for dig in DIGRAPHS:
            self.scat = Sample()
            self.scat.children[0].text = dig
            self.scat.children[0].bind(on_release = self.scat.listen)
            self.digraphs_samp.add_widget(self.scat)

        for consbl in CONSONANTBLENDS:
            self.scat = Sample()
            self.scat.children[0].text = consbl
            self.scat.children[0].bind(on_release = self.scat.listen)
            self.consblends_samp.add_widget(self.scat)


        
class P6Title(Scatter):
    pass



class Dipthongs(MDScreen):

    def __init__(self, **kwargs):
        super(Dipthongs, self).__init__(**kwargs)
        self.dipthongs = self.ids.dipthongs
        self.sound = None
        self.button = None

        for word in DIPTHONGS_EX:
            self.button = MDRaisedButton(text=word,font_size='18sp', size_hint=(None,None))
            self.button.bind(on_press=self.say_word)
            self.dipthongs.add_widget(self.button)
    
    def say_word(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase6/examples/{instance.text}.ogg')
            self.sound.play()

class Digraphs(MDScreen):
    
    def __init__(self, **kwargs):
        super(Digraphs, self).__init__(**kwargs)
        self.digraphs = self.ids.digraphs
        self.sound = None
        self.button = None

        for word in DIGRAPHS_EX:
            self.button = MDRaisedButton(text=word,font_size='18sp', size_hint=(None,None))
            self.button.bind(on_press=self.say_word)
            self.digraphs.add_widget(self.button)
    
    def say_word(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase6/examples/{instance.text}.ogg')
            self.sound.play()

class ConsBlends(MDScreen):
    def __init__(self, **kwargs):
        super(ConsBlends, self).__init__(**kwargs)
        self.consblends = self.ids.consblends
        self.sound = None
        self.button = None

        for word in CONSONANTBLENDS_EX:
            self.button = MDRaisedButton(text=word,font_size='18sp', size_hint=(None,None))
            self.button.bind(on_press=self.say_word)
            self.consblends.add_widget(self.button)
    
    def say_word(self,instance):
        if instance.text:
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase6/examples/{instance.text}.ogg')
            self.sound.play()

class WordOutline(Scatter):
    word = StringProperty("")
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)


class P6Quiz(MDScreen):
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
        zzz = len(self.shown)/30
        self.progress_bar.value = zzz * 100
        if len(self.shown) != 30:
            self.current_answer = random.choice(DIP_DIG_CON_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(DIP_DIG_CON_QUIZ)

            self.word_outline.final_pos = self.word_outline.pos
            x,y = self.word_outline.final_pos
            self.word_outline.pos = (x, y+self.height)
            
            self.word_outline.children[0].source = f"imgs/dip_dig_con/{self.current_answer}.png"
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.word_outline)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL 30 ALREADY ANSWERED')

        self.speaker.theme_icon_color = "Primary"
        self.next_button.disabled = True


    def start_show_word(self, dt):
        if len(self.shown) != 30:
            self.current_answer = random.choice(DIP_DIG_CON_QUIZ)
            while self.current_answer in self.shown:
                self.current_answer = random.choice(DIP_DIG_CON_QUIZ)

    
            self.word_outline.final_pos = self.word_outline.pos
            x,y = self.word_outline.final_pos
            self.word_outline.pos = (x, y+self.height)
            
            self.word_outline.children[0].source = f"imgs/dip_dig_con/{self.current_answer}.png"
            anim1 = Animation(y=y, t='out_bounce')
            anim1.start(self.word_outline)
            self.shown.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL 30 ALREADY ANSWERED')
    

    def on_enter(self):
        Clock.schedule_once(self.start_show_word)

    def validate(self):
        answer = self.answer()
        while not answer:
            self.microphone.disabled = True
            self.microphone.theme_icon_color="Custom"
            self.microphone.icon_color = (0,1,0.3,1)
          
        verify = self.check_answer(f'answers/phase6/{self.answer_file}')
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
        #record = rec(f'answers/phase6/{self.answer_file}', duration, freq)
        record = android_record(f'answers/phase6/{self.answer_file}')
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
            self.sound = SoundLoader.load(f'answers/phase6/{self.answer_file}')
            self.sound.play()
        else:
            print('answer first!') 

class WordOutlineRed(Scatter):
    word = StringProperty("")
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)