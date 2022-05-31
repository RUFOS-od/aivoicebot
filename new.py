import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
from PIL import Image
import subprocess
import pyautogui #screenshot
import pyttsx3
import bs4 as bs
import urllib.request
import requests
#class personne
class person:
    name = ''
    def setName(self, name):
        self.name = name


#class assistant
class asis:
    name = ''
    def setName(self, name):
        self.name = name



def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

#moteur parle
def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer() # initialiser un reconnaisseur
# écouter l'audio et le convertir en texte
def record_audio(ask=""):
    with sr.Microphone() as source: # microphone as source
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5)  # écouter l'audio via la source
        print("Écoute terminée")
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # erreur : le module de reconnaissance ne comprend pas
            engine_speak("je n'ai pas compris cela")
        except sr.RequestError:
            engine_speak('Désolé, le service est en panne') #erreur : le module de reconnaissance n'est pas connecté
        print(">>", voice_data.lower()) # imprimer ce que l'utilisateur a dit
        return voice_data.lower()

# obtenir une chaîne et créer un fichier audio à lire
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='fr-FR') # synthèse vocale (voix)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # sauvegarder entand que mp3
    playsound.playsound(audio_file) # lire le fichier audio
    print(asis_obj.name + ":", audio_string) # imprimer ce que l'application a dit
    os.remove(audio_file) # supprimer le fichier audio

def respond(voice_data):
    # 1 : salutation
    if there_exists(['Salut','Bonjour','hello']):
        greetings = ["Salut, comment puis-je vous aider ?" + person_obj.name, "Salut comment allez-vous?" + person_obj.name, "Je suis à votre écoute" + person_obj.name, "Que desirez-vous?" + person_obj.name, "coucou" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)



     #13 screenshot
    if there_exists(["capture","mon écran","capture d'écran"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screenshot/screen.png')
    
    
     #14 pour rechercher sur wikipedia les définitions
    if there_exists(["définition de"]):
        definition=record_audio("De quoi avez-vous besoin de la définition de")
        url=urllib.request.urlopen('https://fr.wikipedia.org/wiki/'+definition)
        soup=bs.BeautifulSoup(url,'lxml')
        definitions=[]
        for paragraph in soup.find_all('p'):
            definitions.append(str(paragraph.text))
        if definitions:
            if definitions[0]:
                engine_speak("Je suis désolé, je n'ai pas trouvé cette définition, veuillez essayer une recherche sur le Web")
            elif definitions[1]:
                engine_speak("Voici ce que j'ai trouver"+definitions[1])
            else:
                engine_speak ("Voici ce que j'ai trouver"+definitions[2])
        else:
                engine_speak("Désolé je n'ai pas pu trouver la definition de "+definition)


    if there_exists(["sortie", "arrêter", "au revoir"]):
        engine_speak("au revoir")
        exit()

    # # Ville ou région actuelle
    # if there_exists(["Où suis-je"]):
    #     Ip_info = requests.get('https://api.ipdata.co?api-key=test').json() #api a changer
    #     loc = Ip_info['région']
    #     engine_speak(f"Vous devez être quelque part dans {loc}")    
   
   # Emplacement actuel selon Google maps
    if there_exists(["Où suis-je"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        engine_speak("Vous devez être quelque part près d'ici, selon Google Maps")    



time.sleep(0)

person_obj = person()
asis_obj = asis()
asis_obj.name = 'kakiri'
person_obj.name = ""
engine = pyttsx3.init()


while(1):
    voice_data = record_audio("Enregistrement") # obtenir l'entrée vocale
    print("Raire")
    print("Q:", voice_data)
    respond(voice_data) # respond