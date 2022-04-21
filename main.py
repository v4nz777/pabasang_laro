import os
os.environ['KIVY_AUDIO'] = 'ffpyplayer'
from kivy.uix.screenmanager import ScreenManager, Screen
from tinydb import TinyDB, Query





#CONTENTS
from phase1 import IntroToAlphabets, PhaseOneTest
from phase2 import Phoenetics, PhaseTwoTest
from phase3 import TwoLetterWords,TwoLetterWordsLevel2,TwoLetterWordsLevel3
from phase4 import Cvc, VowelA,VowelE,VowelI,VowelO,VowelU, CvcQuiz
from phase5 import CVCandE, CvcQuiz2
from phase6 import Dipthongs, Digraphs, ConsBlends, Phase6Main, P6Quiz
from answers import AnswerP1, AnswerP2, AnswerP3, AnswerP4, AnswerP5, AnswerP6
from kivymd.app import MDApp
#from kivy.core.window import Window
from kivy.lang import Builder
from kivy.clock import Clock
print(Clock.max_iteration)
Builder.load_file("kv.kv")
#Window.size = 640, 360


db = TinyDB('db.json')
Mode = Query()

class MainMenu(Screen):
    def __init__(self, **kw):

        super(MainMenu,self).__init__(**kw)
    def on_toggle(self, instance):
        game_settings = db.search(Mode.name == 'game_settings')
        if game_settings[0]['offline_mode'] == False:
            db.upsert({'offline_mode': True}, Mode.name == 'game_settings')
            instance.icon = "wifi-cancel"
        else:
            db.upsert({'offline_mode': False}, Mode.name == 'game_settings')
            instance.icon = "wifi"



    
class MainMain(ScreenManager):
    def __init__(self, **kwargs):
        super(MainMain, self).__init__(**kwargs)

    def switch(self,x):
        self.current = x



        
    
class PabasangLaro(MDApp):
    def build(self):
        #self.theme_cls.colors = colors
        self.icon = 'bulb.png'
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.accent_palette = "Teal"

        sm = MainMain()
        sm.add_widget(MainMenu(name="MainMenu"))
        sm.add_widget(IntroToAlphabets(name="IntroToAlphabets"))
        sm.add_widget(PhaseOneTest(name="PhaseOneTest"))
        sm.add_widget(Phoenetics(name="Phoenetics"))
        sm.add_widget(PhaseTwoTest(name="PhaseTwoTest"))
        sm.add_widget(TwoLetterWords(name="TwoLetterWords"))
        sm.add_widget(TwoLetterWordsLevel2(name="TwoLetterWordsLevel2"))
        sm.add_widget(TwoLetterWordsLevel3(name="TwoLetterWordsLevel3"))
        sm.add_widget(Cvc(name="Cvc"))
        sm.add_widget(VowelA(name="VowelA"))
        sm.add_widget(VowelE(name="VowelE"))
        sm.add_widget(VowelI(name="VowelI"))
        sm.add_widget(VowelO(name="VowelO"))
        sm.add_widget(VowelU(name="VowelU"))
        sm.add_widget(CvcQuiz(name="CvcQuiz"))
        sm.add_widget(CVCandE(name="CVCandE"))
        sm.add_widget(CvcQuiz2(name="CvcQuiz2"))
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

        return sm

    def on_start(self):
        find_settings = db.search(Mode.name == 'game_settings')
        if find_settings[0] == "":
            print('Creating Game Settings...')
            db.insert({'name': 'game_settings', 'offline_mode': True})
        else:
            print('Loading Game Settings...')

        answers_paths = ['answers/phase1','answers/phase2','answers/phase3','answers/phase4','answers/phase5','answers/phase6']
        for _path in answers_paths:
            if os.path.exists(_path):
                print(f"path: {_path} already exist")
            else:
                print(f'creating directory... :>> {_path}')
                os.makedirs(_path)
                print(_path + " Created!")

 

        return super().on_start()
    
    

    


if __name__ == "__main__":
    PabasangLaro().run()