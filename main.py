
'''
    Python 3.9.4 Used
'''

import os


from threading import Thread, Event, Timer
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
import json
from last import LastScreen


#CONTENTS
from phase1 import IntroToAlphabets, PhaseOneTest
from phase2 import  PhaseTwoTest, PhonogramAlpha
from phase3 import TwoLetterWords,TwoLetterWordsLevel3
from phase4 import Cvc, VowelA,VowelE,VowelI,VowelO,VowelU, VowelALong,VowelELong,VowelILong,VowelOLong,VowelULong,CvcQuiz
from phase5 import CVCandE, CvcQuiz2, CVCStory
from phase6 import Dipthongs, Digraphs, ConsBlends, Phase6Main, P6Quiz
from phase7 import Comprehension, Exercise1, Exercise2, Exercise3, Exercise4, Exercise5, Exercise6, Exercise7, Exercise8, Exercise9
from last import LastScreen
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from answers import AnswerP1, AnswerP2, AnswerP3, AnswerP4, AnswerP5, AnswerP6, AnswerP7
from kivymd.app import MDApp
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.clock import Clock
from time import sleep, time
from materials import FILIPINO_ALPHABETS
Builder.load_file("kv.kv")
#Window.size = 640, 360
from kivy.utils import platform

KIVY_NO_CONFIG = True
KIVY_NO_FILELOG = True






class MainMenu(MDScreen):
    def __init__(self, **kw):
        super(MainMenu, self).__init__(**kw)
        self.name = "MainMenu"
    

    
class MainMain(ScreenManager):
    def __init__(self, **kwargs):
        super(MainMain, self).__init__(**kwargs)

    def switch(self,screen, direction):
        if self.current == "Exercise9":
            self.current = "LastScreen"
            self.transition.direction = "down"
        else:
            self.current = screen
            self.transition.direction = direction
    
    def load_sound(self,source):
        if __name__ == "__main__":
            sound = SoundLoader.load(source)
            sound.play()
            

    def play_sound(self,sauce):
        # thread = Thread(target=self.load_sound, args=(sauce,))
        # thread.start()
        # thread.join()
        
        # event = Event()
        # event.wait(5)S

        # return True
        self.load_sound(sauce)

        
            

   



        
    
class PabasangLaro(MDApp):
    def build(self):
        #self.theme_cls.colors = colors
        self.icon = 'bulb.png'
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.accent_palette = "DeepOrange"

        sm = MainMain()
        sm.add_widget(MainMenu(name="MainMenu"))
        sm.add_widget(IntroToAlphabets(name="IntroToAlphabets"))
        sm.add_widget(PhaseOneTest(name="PhaseOneTest"))
 
        sm.add_widget(PhonogramAlpha(name="PhonogramAlpha"))

        sm.add_widget(PhaseTwoTest(name="PhaseTwoTest"))
        sm.add_widget(TwoLetterWords(name="TwoLetterWords"))
        sm.add_widget(TwoLetterWordsLevel3(name="TwoLetterWordsLevel3"))
        sm.add_widget(Cvc(name="Cvc"))
        sm.add_widget(VowelA(name="VowelA"))
        sm.add_widget(VowelE(name="VowelE"))
        sm.add_widget(VowelI(name="VowelI"))
        sm.add_widget(VowelO(name="VowelO"))
        sm.add_widget(VowelU(name="VowelU"))
        sm.add_widget(VowelALong(name="VowelALong"))
        sm.add_widget(VowelELong(name="VowelELong"))
        sm.add_widget(VowelILong(name="VowelILong"))
        sm.add_widget(VowelOLong(name="VowelOLong"))
        sm.add_widget(VowelULong(name="VowelULong"))
        sm.add_widget(CvcQuiz(name="CvcQuiz"))
        sm.add_widget(CVCandE(name="CVCandE"))
        sm.add_widget(CvcQuiz2(name="CvcQuiz2"))
        sm.add_widget(CVCStory(name="CVCStory"))
        sm.add_widget(Phase6Main(name="Phase6Main"))
        sm.add_widget(Dipthongs(name="Dipthongs"))
        sm.add_widget(Digraphs(name="Digraphs"))
        sm.add_widget(ConsBlends(name="ConsBlends"))
        sm.add_widget(P6Quiz(name="P6Quiz"))
        sm.add_widget(AnswerP1(name="AnswerP1"))
        sm.add_widget(AnswerP2(name="AnswerP2"))
        sm.add_widget(AnswerP3(name="AnswerP3"))
        sm.add_widget(AnswerP4(name="AnswerP4"))
        sm.add_widget(AnswerP5(name="AnswerP5"))
        sm.add_widget(AnswerP6(name="AnswerP6"))
        sm.add_widget(AnswerP7(name="AnswerP7"))
        sm.add_widget(Comprehension(name="Comprehension"))
        sm.add_widget(Exercise1(name="Exercise1"))
        sm.add_widget(Exercise2(name="Exercise2"))
        sm.add_widget(Exercise3(name="Exercise3"))
        sm.add_widget(Exercise4(name="Exercise4"))
        sm.add_widget(Exercise5(name="Exercise5"))
        sm.add_widget(Exercise6(name="Exercise6"))
        sm.add_widget(Exercise7(name="Exercise7"))
        sm.add_widget(Exercise8(name="Exercise8"))
        sm.add_widget(Exercise9(name="Exercise9"))
        sm.add_widget(LastScreen(name="LastScreen"))

        return sm

    def on_start(self):

        # ASK PERMNISSION IN ANDROID
        if platform == 'android':
            from android.permissions import request_permissions, Permission, check_permission
            perms = [Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,Permission.INTERNET, Permission.RECORD_AUDIO, Permission.CAPTURE_AUDIO_OUTPUT]
            request_permissions(perms)
            # ADD DIRECTORIES
            answers_paths = [
            '/storage/emulated/0/pb/answers/phase1','/storage/emulated/0/pb/answers/phase2','/storage/emulated/0/pb/answers/phase3','/storage/emulated/0/pb/answers/phase4','/storage/emulated/0/pb/answers/phase5','/storage/emulated/0/pb/answers/phase6'
            ]
            for _path in answers_paths:
                if os.path.exists(_path):
                    print(f"path: {_path} already exist")
                else:
                    print(f'creating directory... :>> {_path}')
                    os.makedirs(_path)
                    print(_path + " Created!")

        else:
            # ADD DIRECTORIES
            answers_paths = [
                'answers/phase1','answers/phase2','answers/phase3','answers/phase4','answers/phase5','answers/phase6'
            ]
            for _path in answers_paths:
                if os.path.exists(_path):
                    print(f"path: {_path} already exist")
                else:
                    print(f'creating directory... :>> {_path}')
                    os.makedirs(_path)
                    print(_path + " Created!")
        
        #CREATE JSONFILE FOR P7
        p7file = 'p7scorecard.json'
        if os.path.exists(p7file):
            print('P7 SCORECARD ALREADY EXIST')
        else:
            print('#CREATE JSONFILE FOR P7')
            #open('p7scorecard.json','w').close()
            with open('p7scorecard.json', 'w') as _scorecard:
                json.dump({"scores_by_screen": []}, _scorecard)
            _scorecard.close()

        return super().on_start()



    
    
    

    


if __name__ == "__main__":
    PabasangLaro().run()