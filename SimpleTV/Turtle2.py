import kivy, sys, random
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.uix.pagelayout import PageLayout
from kivy.properties import ObjectProperty
import subprocess, sys, time, getpass, os
from kivy.uix.popup import Popup
from Turtel import * # If there is a error Ignore
from Turtel import CheckingForShows as aa # If there is a error Ignore

PathToImages = os.path.dirname(os.path.abspath(__file__)) + '\\Images\\'

# TODO > Odakel ce da cita serije, jer /Download/Serije ne postoji kod drugih korisnika

class LogicPart(PageLayout):

    path_to_the_pics = ObjectProperty()
    path_to_the_pics = os.path.dirname(os.path.abspath(__file__)) + '\\Images\\'

    def AddingShow(self, *args):
        self.path_to_the_pics
        the_popup = CustomPopupMore()
        the_popup.open()

    def OpeningMenu(self, one, two):
        global Name
        Name = two
        the_popup = CustomPopupMenu()
        the_popup.open()

class CustomPopupPitcure(Popup):
    pass

class CustomPopupMenu(Popup):

    def WhenPressed(self, one, three):
        Username = getpass.getuser()
        print('It\'s pressed')
        looking_local_start('C:\\Users\\' + Username + '\\Downloads\\', Name, three)
        
        if zombie == []:
            pass
        else:
            the_popup = CustomPopup()
            the_popup.open()

    def AddingPitcure(self, *args):
        another_one(Name)
        the_popup = CustomPopupPitcure()
        the_popup.open()

    def Remove(self, *args):
        removing(Name)
        the_popup = CustomPopupRemove()
        the_popup.open()


class CustomPopupRemove(Popup):
    pass

class CustomPopupSucess(Popup):
    pass

class CustomPopupNoShow(Popup):
    pass

class CustomPopup(Popup):
    pass

class CustomPopupMore(Popup):

    name_of_the_show = ObjectProperty()
    
    def ReadingNew(self, *args):
        krampus = self.name_of_the_show.text
        Username = getpass.getuser()
        CheckingForShows('C:\\Users\\' + Username + '\\Downloads\\Serije', krampus)
        # delete custompopup success nigdje ga ne koristits

class TurtelKVApp(App):

    def build(self):
        return LogicPart()


if __name__ == '__main__':

    helloKivy = TurtelKVApp()
    helloKivy.run()