from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import kivy
from kivy.uix.popup import Popup

kivy.require('1.10.1')

class TelaPrincipal(BoxLayout):
    pass

# Cria e executa a interface
class Interface(App):
    def build(self):
        self.title = "PRODUTOR/CONSUMIDOR WIN"
        return TelaPrincipal()

run = Interface()
run.run()
