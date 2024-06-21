#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install nltk')
import nltk
import nltk.corpus


# In[2]:


#tokenization

from nltk.tokenize import word_tokenize
chess = "Samay Raina is the best chess player in the world"
word_tokenize(chess)


# In[3]:


#sentence tokenizer

from nltk.tokenize import sent_tokenize
chess2="Samay Raina is the best chess streamer in the world. Sagar Shah is the best chess coach in the world."
sent_tokenize(chess2)


# In[4]:


len(word_tokenize(chess))


# In[5]:


#n-grams
#It calculates the probabilities of words that will come afterward

astro ="Can anybody hear me or am i talking to myself? My mind is running empty in the search for someone else"
astro_tk=(word_tokenize(astro))
list(nltk.bigrams(astro_tk))


# In[6]:


list(nltk.trigrams(astro_tk))


# In[7]:


list(nltk.ngrams(astro_tk,5))


# In[8]:


#stemming

from nltk.stem import PorterStemmer
my_stem= PorterStemmer()

#to find the root word
my_stem.stem("shopping")


# In[9]:


#pos-tagging--partsOfSpeech
'''nnp--proper noun
vbz--verb
dt--determiner/article
jjs--superlative adj
nn--noun...'''


nltk.download('averaged_perceptron_tagger')
tom="Tom Hanks is the best actor in the world"
tom_tk=word_tokenize(tom)
nltk.pos_tag(tom_tk)


# In[10]:


#named entity recognition


nltk.download('words')
nltk.download('maxent_ne_chunker')

from nltk import ne_chunk
pres="Obama was the 44th president of America"
pres_tk=word_tokenize(pres)

pres_pos=nltk.pos_tag(pres_tk)
print(ne_chunk(pres_pos))


# Text-to-speech

# In[11]:


get_ipython().system('pip install gTTS')


# In[12]:


from gtts import gTTS
from IPython.display import Audio #to play some audio

tts=gTTS(input())
tts.save('1.wav')  #tts to wav file
soun='1.wav'
Audio(soun,autoplay=True)  #playing wav file using audio method


# In[14]:


get_ipython().system('pip install pyttsx3')


# In[15]:


#import library
import pyttsx3 
#if any error when installation install the dependency library, If you receive errors such as No module named win32com.client, No module named win32, or No module named win32api, you will need to additionally install pypiwin32.     
engine = pyttsx3.init()     #declare 

#engine.say("I will speak this text")  #pass any string 
engine.runAndWait()  #output in voice format

# Changing Voice , Rate and Volume

import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                    	#printing current voice rate
engine.setProperty('rate', 125) 	# setting up new voice rate

#####VOLUME#####
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                      	#printing current volume level
engine.setProperty('volume',1.0)	# setting up volume level  between 0 and 1

#####VOICE#####
voices = engine.getProperty('voices')   	#getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

sen=engine.say(input())
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

#####Saving Voice to a file#####
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file(sen, 'test.mp3')
engine.runAndWait()


# In[17]:


import pyttsx3
  
def onStart():
   print('starting')
  
def onWord(name, location, length):
   print('word', name, location, length)
  
def onEnd(name, completed):
   print('finishing', name, completed)
  
engine = pyttsx3.init()
  
engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
  
sen = 'Hello Prasuna'
  
  
engine.say(sen)
engine.runAndWait()

