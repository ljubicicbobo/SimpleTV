#! python3
# This is simple program that plays the last episode you watched

import os, re, subprocess, sys, json, glob, random, shutil
import requests, time, urllib, getpass, fnmatch, bs4, getpass
from collections import defaultdict
from qbittorrent import Client # Ovo trebas dodati u setup

# I expect that you have VLC and that it is installed in C:\\Program Files\\VideoLAN\\VLC\\vlc.exe' line 94
# TODO > Odaberi par dan i napravi class za ovo biti ce puno funkcionalni i lakse za ove koje se ponavljaju

zombie = []
FolderPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'UserData\\')
PitcurePath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Images\\')
KivyPath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'TurtelKV.kv')

def looking_local_start(directory, NameOfTheShow, bit):

    # TODO > Problem je sto vidi direktorijum 4 sezona i ude u njega

    try:
        zombie.remove('1')
    except ValueError:
        pass
        
    global ReadingTxt
    ReadingTxt = NameOfTheShow + '.txt'

    sonnetFile = open(FolderPath + NameOfTheShow + '\\' + ReadingTxt)
    Dict = sonnetFile.readlines()
    Season = Dict[1]
    Episode = Dict[0]
    sonnetFile.close()
    altered_carbon = int(Episode)
    if bit == '1':
        altered_carbon = 1 + int(Episode)
        sonnetFileWrite = open(FolderPath + NameOfTheShow + '\\' + ReadingTxt, 'w')
        sonnetFileWrite.write(str(altered_carbon) + '\n' + str(Season))
        sonnetFileWrite.close()

    global IndexNumber
    IndexNumber = NameOfTheShow

    global ImeSezoneUpdated
    SeasonUpd = int(Season) + 1

    if 10 == int(Episode) + 1 or 10 < int(Episode) + 1:
        Monkey = 'E'
    else:
        Monkey = 'E0'
 
    if 10 == int(Season) + 1 or 10 < int(Season) + 1:
        ImeSerije = IndexNumber + '.S' + Season + Monkey + str(altered_carbon)
        ImeSezone = IndexNumber + '.S' + Season # We need ImeSezone to search for folders
        ImeSezoneUpdated = IndexNumber + '.S' + str(SeasonUpd)

    else:
        ImeSerije = IndexNumber + '.S0' + Season + Monkey + str(altered_carbon)
        ImeSezone = IndexNumber + '.S0' + Season
        ImeSezoneUpdated = IndexNumber + '.S0' + str(SeasonUpd)

    print(ImeSerije)
    FirstAustria = [] 
    # We first search for file in directory, if we don't find it 
    # we start searching in all subdirectories
    # we do this by appending to FirstAustria, 1 means positiv
    for i in os.listdir(directory):
        try:
            SearchRegex = re.compile(ImeSerije + '.*' + '.(mkv|mp4)$', re.DOTALL | re.I)
            mo = SearchRegex.search(i)
            FileName = ''.join(mo.group())
            subprocess.Popen(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', directory + '\\' + FileName])
            FirstAustria.append(1)

        except AttributeError:
            pass

    if FirstAustria == []:
        for folderName, subforlder, filenames in os.walk(directory): # Za 100 problem je sto trazi direktorij a ne file

            for subforlders in subforlder:
                ''.join(subforlders)

            for filename in filenames:
                try:
                    SearchRegex = re.compile(ImeSerije + '.*' + '.(mkv|mp4)$', re.DOTALL | re.I)
                    mo = SearchRegex.search(filename)
                    SecondPart = mo.group()
                    FirstPart = folderName
                except AttributeError:
                    pass
 
        try:
            FullName = FirstPart + '\\' + SecondPart
            print(FullName)
            subprocess.Popen(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', FullName])
            print('Playing')
        except UnboundLocalError:
            if bit == '1':
                sonnetFile = open(FolderPath + '\\' + NameOfTheShow + '\\' + ReadingTxt)
                altered_carbon = sonnetFile.readlines()[0]
                Fixing = int(altered_carbon) - 1
                sonnetFile.close()
    
                sonnetFileWrite = open(FolderPath + '\\' + NameOfTheShow + '\\' + ReadingTxt, 'w')
                sonnetFileWrite.write(str(Fixing) + '\n' + Season)
                sonnetFileWrite.close()
            Username = getpass.getuser()
            UpdatingSeason('C:\\Users\\' + Username + '\\Downloads\\', NameOfTheShow)

def UpdatingSeason(directory, NameOfTheShow):

    sonnetFile = open(FolderPath + NameOfTheShow + '\\' + ReadingTxt)
    SeasonNumber = sonnetFile.readlines()[1]
    SeasonNumber = int(SeasonNumber) + 1
    
    ImeSerije = IndexNumber + '.S0' + str(SeasonNumber) + 'E01'
    print('Updated season sucesfully')

    for folderName, subforlder, filenames in os.walk(directory):
        try:
            SearchFolderName = re.compile('.*' + ImeSezoneUpdated + '.*', re.DOTALL | re.I)
            mo1 = SearchFolderName.search(folderName)
            FirstPart = ''.join(mo1.group())
        except AttributeError:
            pass

        for subforlders in subforlder:
            ''.join(subforlders)

        for filename in filenames:
            try:
                SearchRegex = re.compile(ImeSerije + '.*' + '.(mkv|mp4)$', re.DOTALL | re.I)
                mo = SearchRegex.search(filename)
                SecondPart = ''.join(mo.group())
            except AttributeError:
                pass

    try:
        FullName = FirstPart + '\\' + SecondPart
        sonnetFileWrite = open(FolderPath + NameOfTheShow + '\\' + ReadingTxt, 'w')
        sonnetFileWrite.write('0' + '\n' + str(SeasonNumber))
        sonnetFileWrite.close()
        subprocess.Popen(['C:\\Program Files\\VideoLAN\\VLC\\vlc.exe', FullName])
    except:
        zombie.append('1')

def CheckingForShows(directory, krampus):
    
    ForImage = re.compile(' ')
    ForImageSub = ForImage.sub('+', krampus)
    SearchRegex = re.compile(' ')
    ImeSerije = SearchRegex.sub('.', krampus)
    AdddingNewShow(ImeSerije, ForImageSub)

def AdddingNewShow(ImeSerije, ForPitcure):
    os.makedirs(FolderPath + ImeSerije)

    PathSeries = FolderPath + ImeSerije
    Making = open(PathSeries + '\\' + ImeSerije + '.txt', 'w')
    Making.write('0' + '\n' + '1')
    Making.close()

    ###############
    SiteName = "https://wall.alphacoders.com/api2.0/get.php?auth=64c30044f3662198bc35cea5bd5edf26&method=search&term=%s&width=1920&height=1080" % (ForPitcure)
    response = requests.get(SiteName)
    Data = json.loads(response.text)
    w = Data['wallpapers']
 
    if w[0]['file_type'] == '.jpg':
        urllib.request.urlretrieve(w[0]['url_image'], PathSeries + '\\' + '1' + ".jpg")
        ImagePath = PathSeries + '\\' + '1' + ".jpg"
    else:
        urllib.request.urlretrieve(w[0]['url_image'], PathSeries + '\\' + '1' + ".png")
        ImagePath = PathSeries + '\\' + '1' + ".png"


    sonnetFile = open(KivyPath)
    FullFile = sonnetFile.readlines()
    sonnetFile.close()

    myText = ('''
    Button:
        background_normal: r'%s'
        background_down: r'%s'
        on_press: root.OpeningMenu(self, '%s')
    ''' % (ImagePath, ImagePath, ImeSerije))  # A sta AKo nema Slike

    sonnetFileWrite = open(KivyPath, 'w')
    for line in FullFile:
        sonnetFileWrite.write(line)

    sonnetFileWrite.close()
    sonnetFileAppend = open(KivyPath, 'a')
    sonnetFileAppend.write(myText)
    sonnetFileAppend.close()

def another_one(Name):
    ####################################

    SiteName = "https://wall.alphacoders.com/api2.0/get.php?auth=64c30044f3662198bc35cea5bd5edf26&method=search&term=%s&width=1920&height=1080" % (Name)
    response = requests.get(SiteName)
    Data = json.loads(response.text)
    w = Data['wallpapers']

    number = 0
    for i in w:
        number += 1
    randomInteger = random.randint(1, number - 1)

    PathSeries = FolderPath + Name
    if w[randomInteger]['file_type'] == '.jpg':
        urllib.request.urlretrieve(w[randomInteger]['url_image'], PathSeries + '\\' + '1' + ".jpg")
    else:
        urllib.request.urlretrieve(w[randomInteger]['url_image'], PathSeries + '\\' + '1' + ".png")

def removing(NoTS):
    num = 0
    LineNum = []
    for i in open(KivyPath):
        num +=1
        Reg = re.compile(NoTS)
        RegSearch = Reg.search(i)
        try:
            RegSearch.group()
            LineNum.append(num)
        except AttributeError:
            pass
    
    LineDown = int(LineNum[0]) - 1
    EntCont = []
    num2 = 0
    for line in open(KivyPath):
        num2 += 1
        if LineNum[0] == num2 or LineNum[1] == num2 or LineNum[2] == num2 or LineDown == num2 or LineDown - 1 == num2:
            pass
        else:
            EntCont.append(line)

    sonnetWrite = open(KivyPath, 'w')
    for item in EntCont:
        sonnetWrite.write(item)
        
    sonnetWrite.close()
    shutil.rmtree(FolderPath + NoTS)

def changingEpisode(Name, season, bit):
    PathTo = os.path.join(FolderPath, Name, Name + '.txt')

    if bit == 0:
        # I need FirstSeason so that i dont overwrite episode with the first value that came
        global FirstSeason
        FirstSeason = season

    elif bit == 1:
        # Because the counting starts from 0
        if season == '1':
            WritingTxT = open(PathTo, 'w')
            WritingTxT.write('0' + '\n' + FirstSeason)
            WritingTxT.close()
        else:
            WritingTxT = open(PathTo, 'w')
            WritingTxT.write(season + '\n' + FirstSeason)
            WritingTxT.close()

def MeineEmail(email):
    MyEmail = open(FolderPath + 'email.txt', 'w')
    MyEmail.write(email)
    MyEmail.close()

def DeineEmail(password, email):
    DeineEmail = open(FolderPath + 'email2.txt', 'w')
    DeineEmail.write(password + '\n' + email)

def PirateSearch(bit):
    # TODO > namjesti za seedere

    fileNames = []
    fileDict = defaultdict(list)
    seasonList = []

    for file in os.listdir(FolderPath):
        if fnmatch.fnmatch(file, '*.txt'):
            pass
        else:
            Path = os.path.join(FolderPath, file, file + '.txt')
            robot = re.compile('\.')
            SubRobot = robot.sub('%20', file)
            fileNames.append(SubRobot)

            Opening = open(Path)
            Reading = Opening.readlines()
            Season = Reading[1].strip()
            Episode= int(Reading[0].strip()) + 1

            if 10 <= int(Season):
                if 10 <= int(Episode) :
                    fileDict[SubRobot].append('s' + Season + 'e' + str(Episode))
                else:
                    fileDict[SubRobot].append('s' + Season + 'e0' + str(Episode))

            else:
                if 10 <= int(Episode) :
                    fileDict[SubRobot].append('s0' + Season + 'e' + str(Episode))
                else:
                    fileDict[SubRobot].append('s0' + Season + 'e0' + str(Episode))

            seasonList.append(Season)
            Opening.close()

    print(fileDict)
    zeit = 0
    urlList = []
    for a in fileNames:
        SiteName = requests.get("https://pirateproxy.sh/search/" + fileNames[zeit] + '%20' + fileDict[fileNames[zeit]][0])
        name = bs4.BeautifulSoup(SiteName.text, 'lxml')
        magnet = bs4.BeautifulSoup(SiteName.text, 'lxml')

        elementsList = []
        for i in range(0, 5):
            try:
                elems = name.select('a[class="detLink"]')[i]
                elementsList.append(elems.get('title'))
            except IndexError:
                pass

        if elementsList == []:
            season1 = int(seasonList[zeit]) + 1
            NewSeason(fileNames[zeit], str(season1))

        zeit += 1
        number = 0
        achnung = 0
        for i in elementsList:
            regex = re.compile('720p')
            Search = regex.search(i)
            try:
                Search.group()     
                if achnung == 0:
                    elems = magnet.select('a[title="Download this torrent using magnet"]')[number]
                    urlList.append(elems.get('href'))
                    achnung += 1
            except:
                pass

            number += 1

    Username = getpass.getuser()
    for i in urlList:
        time.sleep(2)
        qb = Client('http://127.0.0.1:8080/')
        qb.login('admin', 'admin')
        dl_path = "C:\\Users\\" + Username + "\\Downloads\\"
        qb.download_from_link(i, savepath=dl_path)

def NewSeason(name1, season):

    urlList = []

    if 10 <= int(season):
        EpisodeNum = 's' + season + 'e01'

    else:
        EpisodeNum = 's0' + season + 'e01'

    print(name1 + EpisodeNum)

    SiteName = requests.get("https://pirateproxy.sh/search/" + name1 + '%20' + EpisodeNum)

    name = bs4.BeautifulSoup(SiteName.text, 'lxml')
    magnet = bs4.BeautifulSoup(SiteName.text, 'lxml')

    elementsList = []
    for i in range(0, 5):
        try:
            elems = name.select('a[class="detLink"]')[i]
            elementsList.append(elems.get('title'))
        except IndexError:
            pass

    number = 0
    achnung = 0
    for i in elementsList:
        regex = re.compile('720p')
        Search = regex.search(i)
        try:
            Search.group()     
            if achnung == 0:
                elems = magnet.select('a[title="Download this torrent using magnet"]')[number]
                urlList.append(elems.get('href'))
                achnung += 1
        except:
            pass

        number += 1

    Username = getpass.getuser()
    for i in urlList:
        time.sleep(2)
        qb = Client('http://127.0.0.1:8080/')
        qb.login('admin', 'admin')
        dl_path = "C:\\Users\\" + Username + "\\Downloads\\"
        qb.download_from_link(i, savepath=dl_path)


def UsbTransfer(directory, drive, NameOfTheShow, bit):
    try:
        zombie.remove('1')
    except ValueError:
        pass
        
    global ReadingTxt
    ReadingTxt = NameOfTheShow + '.txt'

    sonnetFile = open(FolderPath + NameOfTheShow + '\\' + ReadingTxt)
    Dict = sonnetFile.readlines()
    Season = Dict[1]
    Episode = Dict[0]
    sonnetFile.close()
    altered_carbon = int(Episode)
    if bit == '1':
        altered_carbon = 1 + int(Episode)
        sonnetFileWrite = open(FolderPath + NameOfTheShow + '\\' + ReadingTxt, 'w')
        sonnetFileWrite.write(str(altered_carbon) + '\n' + str(Season))
        sonnetFileWrite.close()

    global IndexNumber
    IndexNumber = NameOfTheShow

    global ImeSezoneUpdated
    SeasonUpd = int(Season) + 1

    if 10 == int(Episode) + 1 or 10 < int(Episode) + 1:
        Monkey = 'E'
    else:
        Monkey = 'E0'
 
    if 10 == int(Season) + 1 or 10 < int(Season) + 1:
        ImeSerije = IndexNumber + '.S' + Season + Monkey + str(altered_carbon)
        ImeSezone = IndexNumber + '.S' + Season # We need ImeSezone to search for folders
        ImeSezoneUpdated = IndexNumber + '.S' + str(SeasonUpd)

    else:
        ImeSerije = IndexNumber + '.S0' + Season + Monkey + str(altered_carbon)
        ImeSezone = IndexNumber + '.S0' + Season
        ImeSezoneUpdated = IndexNumber + '.S0' + str(SeasonUpd)

    print(ImeSerije)
    FirstAustria = [] 
    # We first search for file in directory, if we don't find it 
    # we start searching in all subdirectories
    # we do this by appending to FirstAustria, 1 means positiv
    for i in os.listdir(directory):
        try:
            SearchRegex = re.compile(ImeSerije + '.*' + '.(mkv|mp4)$', re.DOTALL | re.I)
            mo = SearchRegex.search(i)
            FileName = ''.join(mo.group())
            shutil.move(FileName, drive + '\\')
            FirstAustria.append(1)

        except AttributeError:
            pass

    if FirstAustria == []:
        for folderName, subforlder, filenames in os.walk(directory): # Za 100 problem je sto trazi direktorij a ne file

            for subforlders in subforlder:
                ''.join(subforlders)

            for filename in filenames:
                try:
                    SearchRegex = re.compile(ImeSerije + '.*' + '.(mkv|mp4)$', re.DOTALL | re.I)
                    mo = SearchRegex.search(filename)
                    SecondPart = mo.group()
                    FirstPart = folderName
                except AttributeError:
                    pass
 
        try:
            FullName = FirstPart + '\\' + SecondPart
            print(FullName)
            shutil.move(FullName, drive + '\\')
            print('Playing')
        except UnboundLocalError:
            if bit == '1':
                sonnetFile = open(FolderPath + '\\' + NameOfTheShow + '\\' + ReadingTxt)
                altered_carbon = sonnetFile.readlines()[0]
                Fixing = int(altered_carbon) - 1
                sonnetFile.close()

                sonnetFileWrite = open(FolderPath + '\\' + NameOfTheShow + '\\' + ReadingTxt, 'w')
                sonnetFileWrite.write(str(Fixing) + '\n' + Season)
                sonnetFileWrite.close()

            sonnetFile = open(FolderPath + NameOfTheShow + '\\' + ReadingTxt)
            SeasonNumber = sonnetFile.readlines()[1]
            SeasonNumber = int(SeasonNumber) + 1

