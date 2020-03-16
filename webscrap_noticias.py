
from gtts import gTTS
from playsound import playsound
import requests
import random
import webbrowser


def noticias():
	url = ('https://newsapi.org/v2/top-headlines?'
		   'country=br&'
		   'apiKey=05d5ce74721c41698d58009213297db9')
	req = requests.get(url, timeout=3000)
	json = req.json()
	# PERCORRENDO AS 10 PRIMEIRAS NOTÍCIAS
	for c in range(10):
		print('Notícia ' + str(c + 1))
		print(json['articles'][c]['title'])
		print(json['articles'][c]['description'])

noticias()