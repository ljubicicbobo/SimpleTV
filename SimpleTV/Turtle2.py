import kivy, sys, random
kivy.require('1.10.0')

from os.path import exists
from kivy.app import App
from kivy.uix.button import Label
from kivy.uix.widget import Widget
from kivy.uix.pagelayout import PageLayout
from kivy.properties import ObjectProperty
import subprocess, sys, time, getpass, os, threading
from kivy.uix.popup import Popup
from Turtel import * # If there is a error Ignore
from Turtel import CheckingForShows as aa # If there is a error Ignore

PathToImages = os.path.dirname(os.path.abspath(__file__)) + '\\Images\\'

# TODO > Sta uraditi sa Email 

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

    def change(self, *args):
        the_popup = CustomPopupChange()
        the_popup.open()

    def email(self, *args):
        the_popup = CustomPopupEmail()
        the_popup.open()

    def switchOn(self, instance, value):
        if value is True:
            if exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'UserData', 'email.txt')):
                threadObj = threading.Thread(target=PirateSearch, args=['0'])
                threadObj.start()
            else:
                the_popup = CustomPopupEmail()
                the_popup.open()
        else:
            threadControl.remove(1)
            threadControl.append(2)
        

class CustomPopupEmail(Popup):

    email = ObjectProperty()
    
    def MyEmail(self, *args):
        email = self.email.text
        MeineEmail(email)

    def SendMail(self, *args):
        the_popup = CustomPopupEmail2()
        the_popup.open()

class CustomPopupEmail2(Popup):

    emailTwo = ObjectProperty()
    password = ObjectProperty()

    def MyEmail(self, *args):
        email = self.emailTwo.text
        password = self.password.text
        DeineEmail(password, email)

class CustomPopupChange(Popup):
    
    season = ObjectProperty()

    def ChangingSeason(self, *args):
        season_num = self.season.text
        if season_num == 'exit':
            pass
        else:       
            changingEpisode(Name, season_num, 0)

    def ChangingEpisode(self, *args):
        the_popup = CustomPopupChangeEpisode()
        the_popup.open()

class CustomPopupChangeEpisode(Popup):
        
    episode = ObjectProperty()

    def ChangingEpisode(self, *args):
        episode_num = self.episode.text
        if episode_num == 'exit':
            pass
        else:
            changingEpisode(Name, episode_num, 1)


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


helloKivy = TurtelKVApp()
helloKivy.run()