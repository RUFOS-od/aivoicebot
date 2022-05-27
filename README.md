# Assistant vocal Alexis

Application Python qui utilise la reconnaissance vocale et la synthèse vocale
Cette application utilisait initialement l'API de synthèse vocale de Google, mais a été mise à jour pour utiliser la synthèse vocale hors ligne avec pyttsx3

### Dépendances

```
pip installer la reconnaissance vocale
pip installer pyttsx3
pip installer pyaudio
pip installer playsound
pip installer PyObjC
```
```
pip installer PyAudio
```
(S'il y a un problème lors de l'installation de PyAudio, utilisez le fichier .whl à partir de ce lien [https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio](https://www.lfd.uci.edu/ ~gohlke/pythonlibs/#pyaudio))

### Commandes vocales

Vous pouvez ajouter d'autres commandes, mais ce sont celles qui existent

- Quel est ton nom?
- Quelle heure est-il
- Recherche
- Trouver l'emplacement
- Sortie

### Apple Mac OS X (Homebrew & PyAudio)
Utilisez Homebrew pour installer la bibliothèque portaudio prérequise, puis installez PyAudio en utilisant pip :

`brew install portaudio`
`pip installer pyaudio`

Remarques:

S'il n'est pas déjà installé, téléchargez Homebrew.
pip téléchargera la source PyAudio et la construira pour votre version de Python.
Homebrew et la construction de PyAudio nécessitent également l'installation des outils de ligne de commande pour Xcode (plus d'informations).

https://people.csail.mit.edu/hubert/pyaudio/