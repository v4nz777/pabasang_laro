from kivymd.uix.screen import MDScreen
from kivy.graphics import Rectangle, Color
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, BooleanProperty, ListProperty
from materials import CONSONANTS, CONSONANTS_1, CONSONANTS_2, VOWELS, CONSONANTS_EZ
from kivy.metrics import dp
import random
from kivy.clock import Clock
from materials import understand_tlw
import speech_recognition as sr
#from sound_recorder import rec
from jniusrecord import android_record
from tinydb import TinyDB, Query
from kivy.core.window import Window


class TwoLetterWords(MDScreen):
    blank_1 = ObjectProperty(None)
    blank_2 = ObjectProperty(None)
    consonants = ObjectProperty(None)
    vowels = ObjectProperty(None)

    def __init__(self, **kw):
        super(TwoLetterWords, self).__init__(**kw)

        for consonant in CONSONANTS:
            self.create_scat = Cons(size_hint=(None, None), size=(dp(55),dp(50)), letter=consonant.lower())
            self.create_scat.add_widget(Image(size=(dp(55),dp(50))))

            # if consonant == "ñ".upper():
            #     self.create_scat.children[0].source = f'imgs/letter_blocks/enye.png'
            # else:
            #     self.create_scat.children[0].source = f'imgs/letter_blocks/{consonant.lower()}.png'

            if consonant == "ñ".upper() or consonant == "ng".upper():
                continue
            self.create_scat.children[0].source = f'imgs/letter_blocks/{consonant.lower()}.png'

            self.consonants.add_widget(self.create_scat)
        
        for vowel in VOWELS:
            self.create_scat = Vowl(size_hint=(None, None), size=(dp(55),dp(50)), letter=vowel.lower())
            self.create_scat.add_widget(Image(size=(dp(55),dp(50))))

            self.create_scat.children[0].source = f'imgs/letter_blocks/{vowel.lower()}.png'

            self.vowels.add_widget(self.create_scat)



class Cons(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty("")
    sound = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Cons,self).__init__(**kwargs)
        self.initial_pos = self.pos
        self.auto_bring_to_front = False
        self.size_hint = (None,None)
        self.do_rotation = False
        self.do_scale = False
        

    def on_touch_up(self, touch):
        target1 = self.parent.parent.parent.parent.blank_1
        target2 = self.parent.parent.parent.parent.blank_2

        if self.collide_widget(target1):
            if target2.letter_inside.upper() not in CONSONANTS:
                if self.letter == "ñ":
                    target1.children[0].source = f"imgs/letter_blocks/enye.png"
                else:
                    target1.children[0].source = f"imgs/letter_blocks/{self.letter}.png"
                target1.letter_inside = self.letter
                target1.filled = True
                #TODO SOUND
                if target1.filled and target2.filled:
                    print(f'{target1.letter_inside}{target2.letter_inside}')
                    if self.sound:
                        self.sound.stop()
                    self.sound = SoundLoader.load(f'src/phase3/{target1.letter_inside}{target2.letter_inside}.ogg')
                    self.sound.play()
            
        elif self.collide_widget(target2):
            if target1.letter_inside.upper() not in CONSONANTS:
                if self.letter == "ñ":
                    target2.children[0].source = f"imgs/letter_blocks/enye.png"
                else:
                    target2.children[0].source = f"imgs/letter_blocks/{self.letter}.png"
                target2.letter_inside = self.letter
                target2.filled = True
                #TODO SOUND
                if target1.filled and target2.filled:
                    print(f'{target1.letter_inside}{target2.letter_inside}')
                    if self.sound:
                        self.sound.stop()
                    self.sound = SoundLoader.load(f'src/phase3/{target1.letter_inside}{target2.letter_inside}.ogg')
                    self.sound.play()
        

        if touch in self._touches and touch.grab_state:
            touch.ungrab(self)
            del self._last_touch_pos[touch]
            self._touches.remove(touch)
            x,y = self.initial_pos
            self.pos = (x,y)
            #trick to refresh boxes in their places
            temp_size = Window.size
            xx,yy = temp_size
            Window.size = (xx+1,  yy+1)
            #Get to normal size
            Window.size = (xx-1,  yy-1)
            
            

class Vowl(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty("")
    sound = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Vowl,self).__init__(**kwargs)
        self.initial_pos = self.pos
        self.auto_bring_to_front = False
        self.size_hint = (None,None)
        self.do_rotation = False
        self.do_scale = False
    def on_touch_up(self, touch):
        target1 = self.parent.parent.parent.parent.blank_1
        target2 = self.parent.parent.parent.parent.blank_2

        if self.collide_widget(target1):
            
            if target2.letter_inside.upper() not in VOWELS:
                target1.children[0].source = f"imgs/letter_blocks/{self.letter}.png"
                target1.letter_inside = self.letter
                target1.filled = True
                if target1.filled and target2.filled:
                    print(f'{target1.letter_inside}{target2.letter_inside}')
                    if self.sound:
                        self.sound.stop()
                    self.sound = SoundLoader.load(f'src/phase3/{target1.letter_inside}{target2.letter_inside}.ogg')
                    self.sound.play()
            
        elif self.collide_widget(target2):
            if target1.letter_inside.upper() not in VOWELS:
                target2.children[0].source = f"imgs/letter_blocks/{self.letter}.png"
                target2.letter_inside = self.letter
                target2.filled = True
                #TODO SOUND
                if target1.filled and target2.filled:
                    print(f'{target1.letter_inside}{target2.letter_inside}')
                    if self.sound:
                        self.sound.stop()
                    self.sound = SoundLoader.load(f'src/phase3/{target1.letter_inside}{target2.letter_inside}.ogg')
                    self.sound.play()
        

        if touch in self._touches and touch.grab_state:
            touch.ungrab(self)
            del self._last_touch_pos[touch]
            self._touches.remove(touch)
            self.pos = self.parent.pos
            x,y = self.initial_pos
            self.pos = (x,y)
            #trick to refresh boxes in their places
            temp_size = Window.size
            xx,yy = temp_size
            Window.size = (xx+1,  yy+1)
            #Get to normal size
            Window.size = (xx-1,  yy-1)


class Blanky(Scatter):
    letter_inside = StringProperty("")
    filled = BooleanProperty(False)

    def on_touch_down(self, touch):
        self.letter_inside = ""
        self.filled = False
        self.children[0].source = "imgs/letter_blocks/empty.png"
        return super().on_touch_down(touch)

    



###################################### LEVEL 2 ############################################
class TwoLetterWordsLevel2(MDScreen):
    consonants = ObjectProperty(None)

    left_a = ObjectProperty(None)
    left_e = ObjectProperty(None)
    left_i = ObjectProperty(None)
    left_o = ObjectProperty(None)
    left_u = ObjectProperty(None)
    right_a = ObjectProperty(None)
    right_e = ObjectProperty(None)
    right_i = ObjectProperty(None)
    right_o = ObjectProperty(None)
    right_u = ObjectProperty(None)

    def __init__(self, **kw):
        super(TwoLetterWordsLevel2, self).__init__(**kw)
    
        for consonant in CONSONANTS:
            letter = consonant.lower()
            self.create_cons = Consonant(size_hint=(None, None), size=(dp(55),dp(50)), letter=letter)
            # if letter == "ñ":
            #     self.create_cons.add_widget(Image(size=(dp(55),dp(50)), source=f'imgs/letter_blocks/enye.png'))
            # else:
            #     self.create_cons.add_widget(Image(size=(dp(55),dp(50)), source=f'imgs/letter_blocks/{letter}.png'))
            if letter == "ñ" or letter == "ng":
                continue
            self.create_cons.add_widget(Image(size=(dp(55),dp(50)), source=f'imgs/letter_blocks/{letter}.png'))

            self.consonants.add_widget(self.create_cons)

        
            




class Vowel(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty("")
    location = StringProperty("")
    
    # def on_touch_down(self, touch):
    #     self.ids.block_img.source = "imgs/letter_blocks/empty.png"
    #     if touch in self._touches and touch.grab_state:
    #         touch.ungrab(self)
    #         del self._last_touch_pos[touch]
    #         self._touches.remove(touch)

    #     return super().on_touch_down(touch)

class Consonant(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty("")
    sound = ObjectProperty(None)
    collide_to = Vowel()
    def __init__(self, **kwargs):
        super(Consonant,self).__init__(**kwargs)
        self.auto_bring_to_front = False
        self.size_hint = (None,None)
        self.do_rotation = False
        self.do_scale = False

    def on_touch_up(self, touch):
        left_a = self.parent.parent.parent.left_a
        left_e = self.parent.parent.parent.left_e
        left_i = self.parent.parent.parent.left_i
        left_o = self.parent.parent.parent.left_o
        left_u = self.parent.parent.parent.left_u
        right_a = self.parent.parent.parent.right_a
        right_e = self.parent.parent.parent.right_e
        right_i = self.parent.parent.parent.right_i
        right_o = self.parent.parent.parent.right_o
        right_u = self.parent.parent.parent.right_u

        

        ##################LEFT!!!!!!!!!!!!!!!!!!!!!
        if self.collide_widget(left_a):  
            print(f'{self.letter}a')
            left_a.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/{self.letter}a.ogg')
            self.sound.play()

        elif self.collide_widget(left_e):
            print(f'{self.letter}e')
            left_e.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/{self.letter}e.ogg')
            self.sound.play()

        elif self.collide_widget(left_i):
            print(f'{self.letter}i')
            left_i.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/{self.letter}i.ogg')
            if self.sound:
                self.sound.stop()
            self.sound.play()
        
        elif self.collide_widget(left_o):
            print(f'{self.letter}o')
            left_o.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/{self.letter}o.ogg')
            self.sound.play()

        elif self.collide_widget(left_u):
            print(f'{self.letter}u')
            left_u.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/{self.letter}u.ogg')
            self.sound.play()

        ##################RIGHT!!!!!!!!!!!!!!!!!!!!!

        elif self.collide_widget(right_a):  
            print(f'a{self.letter}')
            right_a.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/a{self.letter}.ogg')
            self.sound.play()

        elif self.collide_widget(right_e):
            print(f'e{self.letter}')
            right_e.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/e{self.letter}.ogg')
            self.sound.play()

        elif self.collide_widget(right_i):
            print(f'i{self.letter}')
            right_i.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/i{self.letter}.ogg')
            self.sound.play()

        elif self.collide_widget(right_o):
            print(f'o{self.letter}')
            right_o.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/o{self.letter}.ogg')
            self.sound.play()

        elif self.collide_widget(right_u):
            print(f'u{self.letter}')
            right_u.children[0].source = f'imgs/letter_blocks/{self.letter}.png'
            self.sound = SoundLoader.load(f'src/phase3/u{self.letter}.ogg')
            self.sound.play()


        if touch in self._touches and touch.grab_state:
            touch.ungrab(self)
            del self._last_touch_pos[touch]
            self._touches.remove(touch)
            self.pos = self.parent.pos
            x,y = self.initial_pos
            self.pos = (x,y)
            #trick to refresh boxes in their places
            temp_size = Window.size
            xx,yy = temp_size
            Window.size = (xx+1,  yy+1)
            #Get to normal size
            Window.size = (xx-1,  yy-1)
        



###################################### LEVEL 3 ############################################
class TwoLetterWordsLevel3(MDScreen):
    first_box = ObjectProperty(None)
    second_box = ObjectProperty(None)
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

    def option_1(self):

        cltr = random.choice(CONSONANTS_EZ)
        vltr = random.choice(VOWELS)
        self.first_box.letter = cltr.lower()
        if self.first_box.letter == "ñ".upper():
            self.first_box.children[0].source = f"imgs/letter_blocks/enye.png"
        else:    
            self.first_box.children[0].source = f"imgs/letter_blocks/{self.first_box.letter}.png"

        
        self.second_box.letter = vltr.lower()
        if self.second_box.letter == "ñ".upper():
            self.second_box.children[0].source = f"imgs/letter_blocks/enye.png"
        else:
            self.second_box.children[0].source = f"imgs/letter_blocks/{self.second_box.letter}.png"

        self.first_box.final_pos = self.first_box.pos
        x,y = self.first_box.final_pos
        self.first_box.pos = (x-self.width,y)
        anim1 = Animation(x=x, size=(80, 80), t='out_bounce')
        anim1.start(self.first_box)

        self.second_box.final_pos = self.second_box.pos
        xx,yy = self.second_box.final_pos
        self.second_box.pos = (xx+self.width,yy)
        anim2 = Animation(x=xx, size=(80, 80), t='out_bounce')
        anim2.start(self.second_box)
        return self.first_box.letter + self.second_box.letter
    
    def option_2(self):

        cltr = random.choice(CONSONANTS_EZ)
        vltr = random.choice(VOWELS)
        self.first_box.letter = vltr.lower()
        if self.first_box.letter == "ñ".upper():
            self.first_box.children[0].source = f"imgs/letter_blocks/enye.png"
        else:
            self.first_box.children[0].source = f"imgs/letter_blocks/{self.first_box.letter}.png"

        self.second_box.letter = cltr.lower()
        if self.second_box.letter == "ñ".upper():
            self.second_box.children[0].source = f"imgs/letter_blocks/enye.png"
        else:
            self.second_box.children[0].source = f"imgs/letter_blocks/{self.second_box.letter}.png"
        
        self.first_box.final_pos = self.first_box.pos
        x,y = self.first_box.final_pos
        self.first_box.pos = (x-self.width,y)
        anim1 = Animation(x=x, size=(80, 80), t='out_bounce')
        anim1.start(self.first_box)

        self.second_box.final_pos = self.second_box.pos
        xx,yy = self.second_box.final_pos
        self.second_box.pos = (xx+self.width,yy)
        anim2 = Animation(x=xx, size=(80, 80), t='out_bounce')
        anim2.start(self.second_box)
        return self.first_box.letter + self.second_box.letter

 
    def next(self):
        choices = [self.option_1, self.option_2]
        zzz = len(self.showed)/10
        self.progress_bar.value = zzz * 100
        if len(self.showed) != 10:
            self.current_answer = random.choice(choices)()
            while self.current_answer in self.showed:
                self.current_answer = random.choice(choices)()

            self.showed.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL Letters ALREADY ANSWERED')
        self.speaker.theme_icon_color = "Primary" 
        self.next_button.disabled = True
    
    def initial(self,dt):
        choices = [self.option_1, self.option_2]
        if len(self.showed) != 10:
            self.current_answer = random.choice(choices)()
            while self.current_answer in self.showed:
                self.current_answer = random.choice(choices)()
                
            self.showed.append(self.current_answer)
            print(self.current_answer)
        else:
            self.toolbar.disabled = False
            print('ALL Letters ALREADY ANSWERED')

    def on_enter(self):
        Clock.schedule_once(self.initial)

    def validate(self):
        answer = self.answer()
        while not answer:
            self.microphone.disabled = True
            self.microphone.theme_icon_color="Custom"
            self.microphone.icon_color = (0,1,0.3,1)
          
        verify = self.check_answer(f'answers/phase3/{self.answer_file}')
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
        #record = rec(f'answers/phase3/{self.answer_file}', duration, freq)
        record = android_record(f'answers/phase3/{self.answer_file}')

        
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
                understand = understand_tlw(self.current_answer, result)
                print(understand)
                return understand[0]
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
            self.sound = SoundLoader.load(f'answers/phase3/{self.answer_file}')
            self.sound.play()
        else:
            print('answer first!')

        
class FirstBox(Scatter):
    letter = StringProperty("")
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)
    
class SecondBox(Scatter):
    letter = StringProperty("")
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)

