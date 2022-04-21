from kivymd.uix.button import MDIconButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivy.uix.screenmanager import ScreenManager, Screen
from tinydb import TinyDB, Query
from kivymd.uix.label import MDLabel, MDIcon
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader, Sound

#CONTENTS
from phase1 import IntroToAlphabets, PhaseOneTest
from phase2 import Phoenetics, PhaseTwoTest
from phase3 import TwoLetterWords,TwoLetterWordsLevel2,TwoLetterWordsLevel3
from phase4 import Cvc, VowelA,VowelE,VowelI,VowelO,VowelU, CvcQuiz
from phase5 import CVCandE, CvcQuiz2
from phase6 import Dipthongs, Digraphs, ConsBlends, Phase6Main, P6Quiz

from kivy.properties import ListProperty
import os



class AnswerP1(Screen):
    sound = None
    directory = ListProperty([])
    def __init__(self, **kw):
        super(AnswerP1, self).__init__(**kw)
        self.table = self.ids.answers_p1
        try:
            self.directory = os.listdir('answers/phase1')
        except:
            self.makedir = os.makedirs('answers/phase1')
            self.directory = os.listdir('answers/phase1')
        for i in self.directory:
            answer = i[-5]
            if i == 'big-NG.amr':
                answer = 'NG'
            elif i == 'small-ng.amr':
                answer = 'ng'
            elif i == 'big-ENYE.amr':
                answer = "Ñ"
            elif i == 'small-enye.amr':
                answer = "Ñ".lower()
            
             
            self.table.add_widget(Label(
                text=answer,
                font_name='NotoSerif-Regular.ttf',
                color=(0,0,.5,1),
                font_size='35sp',
                halign='center'
    
                )
            )

            self.btn = MDIconButton(
                icon='volume-high',
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

    def listen_answer(self, instance):
        answer = instance.text 
        if instance.text.isupper():
            answer = 'big' + '-' + instance.text + '.amr'
        else:
            answer = 'small' + '-' + instance.text + '.amr'
        print(answer)
        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(f'answers/phase1/{answer}')
        self.sound.play()



########################################################################################

class AnswerP2(Screen):
    sound = None
    directory = ListProperty([])
    def __init__(self, **kw):
        super(AnswerP2, self).__init__(**kw)
        self.table = self.ids.answers_p2
        try:
            self.directory = os.listdir('answers/phase2')
        except:
            self.makedir = os.makedirs('answers/phase2')
            self.directory = os.listdir('answers/phase2')
        
        for i in self.directory:
            if i == 'enye.amr':
                answer = 'Ñ'.lower()
            else:
                answer = i.replace('.amr', '')
         
            self.table.add_widget(Label(
                text=answer,
                font_name='NotoSerif-Regular.ttf',
                color=(0,0,.5,1),
                font_size='35sp',
                halign='center'
    
                )
            )

            self.btn = MDIconButton(
                icon='volume-high',
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

    def listen_answer(self, instance):
        answer = instance.text + '.amr'

        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(f'answers/phase2/{answer}')
        self.sound.play()


########################################################################################    

class AnswerP3(Screen):
    sound = None
    directory = ListProperty([])
    def __init__(self, **kw):
        super(AnswerP3, self).__init__(**kw)
        self.table = self.ids.answers_p3
        try:
            self.directory = os.listdir('answers/phase3')
        except:
            self.makedir = os.makedirs('answers/phase3')
            self.directory = os.listdir('answers/phase3')
        for i in self.directory:
            answer = i.replace('.amr', '')
         
            self.table.add_widget(Label(
                text=answer,
                font_name='NotoSerif-Regular.ttf',
                color=(0,0,.5,1),
                font_size='35sp',
                halign='center'
    
                )
            )

            self.btn = MDIconButton(
                icon='volume-high',
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

    def listen_answer(self, instance):
        answer = instance.text + '.amr'

        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(f'answers/phase3/{answer}')
        self.sound.play()

########################################################################################  

class AnswerP4(Screen):
    directory = ListProperty([])
    sound = None
    def __init__(self, **kw):
        super(AnswerP4, self).__init__(**kw)
        self.table = self.ids.answers_p4
        try:
            self.directory = os.listdir('answers/phase4')
        except:
            self.makedir = os.makedirs('answers/phase4')
            self.directory = os.listdir('answers/phase4')

        for i in self.directory:
            answer = i.replace('.amr', '')
         
            self.table.add_widget(Label(
                text=answer,
                font_name='NotoSerif-Regular.ttf',
                color=(0,0,.5,1),
                font_size='35sp',
                halign='center'
    
                )
            )

            self.btn = MDIconButton(
                icon='volume-high',
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

    def listen_answer(self, instance):
        answer = instance.text + '.amr'

        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(f'answers/phase4/{answer}')
        self.sound.play()


########################################################################################  

class AnswerP5(Screen):
    directory = ListProperty([])
    sound = None
    def __init__(self, **kw):
        super(AnswerP5, self).__init__(**kw)
        self.table = self.ids.answers_p5
        try:
            self.directory = os.listdir('answers/phase5')
        except:
            self.makedir = os.makedirs('answers/phase5')
            self.directory = os.listdir('answers/phase5')

        for i in self.directory:
            answer = i.replace('.amr', '')
         
            self.table.add_widget(Label(
                text=answer,
                font_name='NotoSerif-Regular.ttf',
                color=(0,0,.5,1),
                font_size='35sp',
                halign='center'
    
                )
            )

            self.btn = MDIconButton(
                icon='volume-high',
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

    def listen_answer(self, instance):
        answer = instance.text + '.amr'

        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(f'answers/phase5/{answer}')
        self.sound.play()


######################################################################################## 

class AnswerP6(Screen):
    directory = ListProperty([])
    sound = None
    def __init__(self, **kw):
        super(AnswerP6, self).__init__(**kw)
        self.table = self.ids.answers_p6
        try:
            self.directory = os.listdir('answers/phase6')
        except:
            self.makedir = os.makedirs('answers/phase6')
            self.directory = os.listdir('answers/phase6')

        for i in self.directory:
            answer = i.replace('.amr', '')
         
            self.table.add_widget(Label(
                text=answer,
                font_name='NotoSerif-Regular.ttf',
                color=(0,0,.5,1),
                font_size='35sp',
                halign='center'
    
                )
            )

            self.btn = MDIconButton(
                icon='volume-high',
                icon_color=(0,0,.5,1),
                text=answer
                )
            self.btn.bind(on_release=self.listen_answer)
            self.table.add_widget(self.btn)

    def listen_answer(self, instance):
        answer = instance.text + '.amr'

        if self.sound:
            self.sound.stop()
        self.sound = SoundLoader.load(f'answers/phase6/{answer}')
        self.sound.play()


######################################################################################## 