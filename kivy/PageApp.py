from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivi.uix.widget import Widget
from kivi.uix.button import Widget


class PageLayoutApp(App):
    def build(self):
        return RootWidget()


class RootWidget(PageLayout):
    def __init__(self, **kwargs):
         super(RootWidget, self).__init__(**kwargs)
         msp = MySuperButton()
         msp.bind(pressed=self.btn_pressed)
         self.add_widget(msp)

    def btn_pressed(self, instance, pos):
        print ('From the root : pressed at {pos}'.format(pos=pos))

class MySuperButton(Button):

     pressed = ListProperty([0, 0])

     def on_touch_down(self, touch):
         if self.collide_point(*touch.pos):
             self.pressed = touch.pos
             return True
         return super(CustomBtn, self).on_touch_down(touch)

     def on_pressed(self, instance, pos):
         print ('pressed at {pos}'.format(pos=pos))


if __name__ == "__main__":
    pla = PageLayoutApp()
    pla
    
    .run()
