from kivy.app import App
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen



class MainScreen(Screen):

  def __init__(self, **kwargs):
    super(MainScreen, self).__init__(**kwargs)
    self.layout = BoxLayout(orientation="vertical")

    self.label1 = Label(text="Hello")
    self.layout.add_widget(self.label1)

    

    self.add_widget(self.layout)




class MyApp(App):

  def build(self):
    sm = ScreenManager()
    sm.add_widget(MainScreen(name="Main"))
  
    return sm


if __name__ == "__main__":
  MyApp().run()
