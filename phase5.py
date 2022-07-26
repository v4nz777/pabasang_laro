from kivy.app import App
from kivymd.uix.screen import MDScreen
from kivy.uix.carousel import Carousel
from kivy.core.audio import SoundLoader
from kivy.uix.scatter import Scatter
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scatterlayout import ScatterLayout
from kivy.animation import Animation
from kivymd.uix.button.button import MDRectangleFlatButton
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from kivymd.uix.label.label import MDLabel
from kivy.graphics import Line, Color, Rectangle
from kivy.metrics import sp
from kivy.animation import Animation

from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty, StringProperty, ListProperty, BooleanProperty
from materials import CVC2_QUIZ
import random
from kivy.clock import Clock

from sound_recorder import rec
#from jniusrecord import android_record, play_audio
from kivy.utils import platform
from kivy.core.window import Window

class CVCandE(MDScreen):
    cblank = ObjectProperty(None)
    vce_caro = ObjectProperty(None)

    grid_of_consonants = NumericProperty(0)

    ake = ListProperty(['m','l','r','b','s'])
    ate = ListProperty(['m','l','r','f','g','d'])
    ame = ListProperty(['s','f','l','g'])
    ade = ListProperty(['m','f'])
    ale = ListProperty(['m','g','h'])
    aze = ListProperty(['m','g','h','l'])
    age = ListProperty(['m','p','c'])

    ice = ListProperty(['m','l','r','n'])
    ite = ListProperty(['l','r'])
    ike = ListProperty(['l','b'])
    ime = ListProperty(['l','t'])
    ide = ListProperty(['r','h'])

    ope = ListProperty(['h','r'])
    obe = ListProperty(['r','l'])
    ote = ListProperty(['n','v'])
    ole = ListProperty(['m','r','s'])
    ome = ListProperty(['h','d','t'])

    ute = ListProperty(['c','m'])
    ume = ListProperty(['f'])
    use = ListProperty(['f','m'])
    ube = ListProperty(['c','p'])

    ude = ListProperty(['r','d','j'])
    #ube = ListProperty(['c','t','p'])
    une = ListProperty(['j','r','d','t'])

    ey = ListProperty(['ake','ate', 'ame', 'ade', 'ale', 'aze', 'age'])
    ay = ListProperty(['ice','ite', 'ike', 'ime', 'ide'])
    ow = ListProperty(['ope','obe', 'ote', 'ole', 'ome'])
    syu = ListProperty(['une', 'ude'])
    lyu = ListProperty(['ute','ume', 'ube','use'])


    grid = ObjectProperty(None)
    c = ObjectProperty(None)
    vce = ObjectProperty(None)
    vce_label = ObjectProperty(None)
    c_label = ObjectProperty(None)


    target_transformed = BooleanProperty(False)



    def __init__(self, **kw):
        super(CVCandE, self).__init__(**kw)
        self.switch_ey('ake', True)

    def add_consonants(self, consonants_list):
        self.ids.consonants_container.clear_widgets()
        self.ids.consonants_container.cols = len(consonants_list)
        for i in consonants_list:
            consonant = CVCCons()
            self.label=MDLabel()
            self.label.text=i
            self.label.font_name='ShadowsIntoLight-Regular.ttf'
            self.label.halign='center'
            self.label.valign='center'
            self.label.font_size=sp(50)
            self.label.color=(1, 1, 1, 1)

            consonant.add_widget(self.label)
            
            self.ids.consonants_container.add_widget(consonant)
    
    def add_vce(self,vce,slide):
        self.ids.vce_caro.clear_widgets()
        for i in vce:
            parent_anchor = AnchorLayout()
            parent_anchor.anchor_x = "left"
            parent_anchor.size_hint=(1,1)

            v_c_e  = VCe()
            v_c_e.children[0].text = i

            parent_anchor.add_widget(v_c_e)
            self.ids.vce_caro.add_widget(parent_anchor)
        
        for i in self.ids.vce_caro.slides:
            if i.children[0].children[0].text == slide:
                self.ids.vce_caro.load_slide(i)

    def switch_ey(self, slide, init):
        self.cblank.children[0].text = ""
        if slide == "ake":
            consonants = self.ake
        elif slide == 'ate':
            consonants = self.ate
        elif slide == 'ame':
            consonants = self.ame
        elif slide == 'ade':
            consonants = self.ade
        elif slide == 'ale':
            consonants = self.ale
        elif slide == 'aze':
            consonants = self.aze
        elif slide == 'age':
            consonants = self.age

        self.add_consonants(consonants)
        self.add_vce(self.ey, slide)
        if not init:
            self.sound = SoundLoader.load(f"src/phase5/{slide}.ogg")
            if self.sound:
                self.sound.stop()
            self.sound.play()

    def switch_ay(self, slide, init):
        self.cblank.children[0].text = ""
        if slide == 'ice':
            consonants = self.ice
        elif slide == 'ite':
            consonants = self.ite
        elif slide == 'ike':
            consonants = self.ike
        elif slide == 'ime':
            consonants = self.ime
        elif slide == 'ide':
            consonants = self.ide
        self.add_consonants(consonants)
        self.add_vce(self.ay, slide)
        if not init:
            self.sound = SoundLoader.load(f"src/phase5/{slide}.ogg")
            if self.sound:
                self.sound.stop()
            self.sound.play()

        
    def switch_ow(self, slide, init):
        self.cblank.children[0].text = ""
        if slide == 'ope':
            consonants = self.ope
        elif slide == 'obe':
            consonants = self.obe
        elif slide == 'ote':
            consonants = self.ote
        elif slide == 'ole':
            consonants = self.ole
        elif slide == 'ome':
            consonants = self.ome
        self.add_consonants(consonants)
        self.add_vce(self.ow, slide)
        if not init:
            self.sound = SoundLoader.load(f"src/phase5/{slide}.ogg")
            if self.sound:
                self.sound.stop()
            self.sound.play()

        
    def switch_syu(self, slide, init):
        self.cblank.children[0].text = ""
        
        if slide == 'une':
            consonants = self.une
        elif slide == 'ude':
            consonants = self.ude

        self.add_consonants(consonants)
        self.add_vce(self.syu, slide)
        if not init:
            self.sound = SoundLoader.load(f"src/phase5/{slide}.ogg")
            if self.sound:
                self.sound.stop()
            self.sound.play()



    def switch_lyu(self, slide, init):
        self.cblank.children[0].text = ""
        if slide == 'ute':
            consonants = self.ute
        elif slide == 'ume':
            consonants = self.ume
        elif slide == 'use':
            consonants = self.use
        elif slide == 'ube':
            consonants = self.ube
        self.add_consonants(consonants)
        self.add_vce(self.lyu, slide)
        if not init:
            self.sound = SoundLoader.load(f"src/phase5/{slide}.ogg")
            if self.sound:
                self.sound.stop()
            self.sound.play()


class CBlank(Scatter, MagicBehavior):
    def __init__(self, **kwargs):
        super(CBlank, self).__init__(**kwargs)
        self.create()

    def create(self):
        self.clear_widgets()
        self.size_hint= (None, None)
        self.disabled=True
        self.auto_bring_to_front=False
        with self.canvas:
            self.line_color = Color(rgba=(1, 1, 1, 1))
            self.line = Line(width=3,rectangle=(self.x, self.y, self.width, self.height))
        with self.canvas:
            self.rect_color = Color(rgba=(0.5, 0, 0, 1))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        label = MDLabel()
        label.text = ""
        label.size_hint = (1,0.3)
        label.font_name = 'ShadowsIntoLight-Regular.ttf'
        label.font_size = sp(50)
        label.color = (1, 1, 1, 1)
        label.disabled_color = (1, 1, 1, 1)
        label.halign = "center"
        label.valign = "center"
        self.add_widget(label)
    
    def illuminate(self):
        self.line.width = 1
        self.rect_color.rgba = 1,0.5,0,1
        self.line_color.rgba = 1,0.5,0,1
        
    
    def revert(self):
        self.line.width = 2
        self.rect_color.rgba = 0.5, 0, 0, 1
        self.line_color.rgba = 1, 1, 1, 1
    

    def inject(self) -> None:
        """Inject effect animation."""

        (
            (
                Animation(scale_y=0.7, t="out_bounce", d=0.03 / self.magic_speed)
                & Animation(
                    scale_x=1.4, t="out_bounce", d=0.03 / self.magic_speed
                )
            )
            + (
                Animation(scale_y=1, t="out_elastic", d=0.5 / self.magic_speed)
                & Animation(
                    scale_x=1, t="out_elastic", d=0.4 / self.magic_speed
                )
            )
        ).start(self)


class VCeCaro(Carousel):
    sound = ObjectProperty(None)
    def __init__(self, **kwargs):
        super(VCeCaro, self).__init__(**kwargs)
        self.ignore_perpendicular_swipes=True
        self.loop=False
    
    
    def on_touch_down(self, touch):
        pass
    def on_touch_move(self, touch):
        pass
    def on_touch_up(self, touch):
        if self.collide_point(*touch.pos):
            if self.current_slide != self.slides[-1]:
                next_slide = self.next_slide.children[0].children[0]
                self.load_next()
                print(next_slide.text)   

                target_parent = self.parent.parent.parent
                if next_slide.text in target_parent.ey:
                    target_parent.switch_ey(next_slide.text, False)
                elif next_slide.text in target_parent.ay:
                    target_parent.switch_ay(next_slide.text, False)
                elif next_slide.text in target_parent.ow:
                    target_parent.switch_ow(next_slide.text, False)
                elif next_slide.text in target_parent.syu:
                    target_parent.switch_syu(next_slide.text, False)
                elif next_slide.text in target_parent.lyu:
                    target_parent.switch_lyu(next_slide.text, False)
            else:
                print("last slide")
            
            


            return super().on_touch_up(touch)

   
    



class VCe(Scatter, MagicBehavior):
    def __init__(self, **kwargs):
        super(VCe, self).__init__(**kwargs)
        self.create()
    
    def create(self):
        self.clear_widgets()
        self.size_hint= (1, None)
        self.disabled=True
        self.auto_bring_to_front=False
        with self.canvas:
            self.line_color = Color(rgba=(1, 1, 1, 1))
            self.line = Line(width=2,rectangle=(self.x, self.y, self.width, self.height))
        with self.canvas.before:
            self.rect_color = Color(rgba=(0.5, 0, 0, 1))
            self.rect = Rectangle(size=self.size, pos=self.pos)
        
        label = MDLabel()
        label.size_hint = (1,0.3)
        label.font_name = 'ShadowsIntoLight-Regular.ttf'
        label.font_size = sp(45)
        label.color = (1, 1, 1, 1)
        label.disabled_color = (1, 1, 1, 1)
        label.halign = "center"
        label.valign = "center"

        self.add_widget(label)

    def illuminate(self):
        self.line.width = 1
        self.rect_color.rgba = 1,0.5,0,1
        self.line_color.rgba = 1,0.5,0,1
    
    def revert(self):
        self.line.width = 2
        self.rect_color.rgba = 0.5, 0, 0, 1
        self.line_color.rgba = 1, 1, 1, 1





class CVCCons(Scatter):
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    letter = StringProperty("")
    sound = ObjectProperty(None)

    # grid = ObjectProperty(None)
    # grid_spacing = NumericProperty(15)
    # c = ObjectProperty(None)
    # vce = ObjectProperty(None)
    # vce_label = ObjectProperty(None)
    # c_label = ObjectProperty(None)


    # target_transformed = BooleanProperty(False)




    def __init__(self, **kwargs):
        super(CVCCons, self).__init__(**kwargs)

        self.initial_pos = self.pos
        self.auto_bring_to_front = False
        self.size_hint = (None,None)
        self.do_rotation = False
        self.do_scale = False
        with self.canvas:
            Color(rgba=(1, 1, 1, 1))
            Line(width=2,rectangle=(self.x, self.y, self.width, self.height))
        with self.canvas.before:
            Color(rgba=(0, 0.3, 0.2, 1))
            Rectangle(size=self.size, pos=self.pos)
        
    

    def on_touch_up(self, touch):
        parent_main = self.parent.parent.parent.parent
        c = parent_main.cblank
        #self.target_transformed = True
        if self.collide_point(*touch.pos):
            if self.collide_widget(c):
            
            
                grid = parent_main.cvce_target_layout

                vces = parent_main.vce_caro
                vce = vces.children[0].children[0].children[0]

                c_label = c.children[0]
                vce_label = vces.children[0].children[0].children[0].children[0]

                c_letter = self.children[0].text
                vce_letter = vces.children[0].children[0].children[0].children[0].text

                
                print(c_letter + vce_letter)
                if self.sound:
                    self.sound.stop()
                self.sound = SoundLoader.load(f'src/phase5/{c_letter + vce_letter}.ogg')
                self.sound.play()

                c.children[0].text = c_letter

                grid.spacing = 0
                c.illuminate()
                c.inject()
                vce.illuminate()
                vce.wobble()
                vce_label.halign = "left"
                c_label.halign = "right"
                
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
                return super().on_touch_up(touch)
            else:
                #trick to refresh boxes in their places
                # temp_size = Window.size
                # xx,yy = temp_size
                # Window.size = (xx+1,  yy+1)
                # #Get to normal size
                # Window.size = (xx-1,  yy-1)
                return super().on_touch_up(touch)
    
    def on_touch_down(self, touch):
        parent_main = self.parent.parent.parent.parent
        c = parent_main.cblank
        if self.collide_point(*touch.pos):
            txt = self.children[0].text.lower()
            
            if self.sound:
                self.sound.stop()
            self.sound = SoundLoader.load(f'src/phase2/letter_sounds/{txt}.ogg')
            self.sound.play()

            grid = parent_main.cvce_target_layout
            vces = parent_main.vce_caro
            vce = vces.children[0].children[0].children[0]

            c_label = c.children[0]
            vce_label = vces.children[0].children[0].children[0].children[0]
            
            try:
                grid.spacing = 15
                c.revert()
                c.children[0].text = ""
                vce.revert()
                vce_label.halign = "center"
                c_label.halign = "center" 
            except AttributeError:
                print('not yet transformed')

            
            

                #self.target_transformed = False          
        
        return super().on_touch_down(touch)
        




############################# CVC STORY ######################

class CVCStory(MDScreen):
    caro = ObjectProperty(None)
    toolbar= ObjectProperty(None)

class Caro(Carousel):
    def on_touch_move(self, touch):
        if self.index == 4:
            self.parent.parent.toolbar.disabled = False
        return super().on_touch_move(touch)


















############## QUIZ #########################################################################
 
class CvcQuiz2(MDScreen):
    word_outline = ObjectProperty(None)
    current_answer = StringProperty("")
    shown = ListProperty([])
    tries = ListProperty([])

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
        self.sound = SoundLoader.load('src/pre_record_sound.ogg')
        self.sound.play()
        answer = self.answer()
        while not answer:
            #self.microphone = MDSpinner()
            self.microphone.disabled = True
            self.microphone.theme_icon_color="Custom"
            self.microphone.icon = "microphone-question"
            self.microphone.icon_color = (0,1,0.3,1)
          
        
        if self.answer_file in self.tries:
            self.speaker.theme_icon_color="Custom"
            self.speaker.icon_color = (0,1,0.3,1)
            self.next_button.disabled = False

        #then autoplay recorded
        self.listen_answer()
        

    def answer(self):
        self.answer_file = self.current_answer + '.m4a'
        duration = 4
        freq = 44100
        record = rec(f'answers/phase5/{self.answer_file}')
        #record = android_record(f'/storage/emulated/0/pb/answers/phase5/{self.answer_file}')
        self.tries.append(self.answer_file)
        return record


    def listen_answer(self):
        self.answer_file = self.current_answer + '.m4a'

        if self.answer_file in self.tries:
            path_to_file = f'answers/phase5/{self.answer_file}'
            
            if platform == "android":
                path_to_file = f'/storage/emulated/0/pb/answers/phase5/{self.answer_file}'
                play_audio(path_to_file)
            else:
                if self.sound:
                    self.sound.stop()
                self.sound = SoundLoader.load(path_to_file)
                self.sound.play()
        else:
            print('answer first!')   

class WordOutline(Scatter):
    word = StringProperty("")
    xxx = NumericProperty(0)
    yyy = NumericProperty(0)
    initial_pos = ReferenceListProperty(xxx,yyy)
    final_pos = ReferenceListProperty(xxx,yyy)


