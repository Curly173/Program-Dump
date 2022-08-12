'''
MCode Translator.py
@author: Noah Totzke

Description: 
Takes in plain ascii text and translates it to morse code, then plays it out in a 800Hz tone pattern.

08-10-2022: v1.0.0 - Initial Release version
'''

import math
import time
from pyaudio import PyAudio

dict_mcode = {
    "a": "·-", "b": "-···", "c": "-·-·", "d": "-··", "e": "·",
    "f": "··-·", "g": "--·", "h": "····", "i": "··", "j": "·---",
    "k": "-·-", "l": "·-··", "m": "--", "n": "-·", "o": "---",
    "p": "·--·", "q": "--·-", "r": "·-·", "s": "···","t": "-",
    "u": "··-", "v": "···-", "w": "·--", "x": "-··-", "y": "-·--",
    "z": "--··",

    " ": " ", ".": "·-·-·-",

    "1": "·----", "2": "··---", "3": "···--", "4": "····-", "5": "·····",
    "6": "-····", "7": "--···", "8": "---··", "9": "----·", "0": "-----"
}
translen = 50
while translen > 48:
    transcode_word = input("Please enter what you want to be translated.\n (No more than 48 characters)\n").lower().split()

    transcode_letter = []
    for word in transcode_word:
        transcode_letter.extend(word)

    completetrans = []
    for letter in transcode_letter:
        completetrans.append(dict_mcode[letter])
    
    translen = len(completetrans)
    if translen > 48:
        print("Error: Too many characters\n")

compiledtrans = ' '.join(completetrans)

print(compiledtrans, "\n \n Playing morse audio sample (First two indicate beeps the begining)")

mcodextend = []
for sym in completetrans:
   mcodextend.extend(sym)

BITRATE = 16000 #number of frames per second/frameset.

FREQUENCY = 800 #Hz, waves per second
LENGTH = 0.175 #seconds to play sound

NUMBEROFFRAMES = int(BITRATE * LENGTH)
RESTFRAMES = NUMBEROFFRAMES % BITRATE
WAVEDATA = ''

for x in range(NUMBEROFFRAMES):
   WAVEDATA += chr(int(math.sin(x / ((BITRATE / FREQUENCY) / math.pi)) * 127 + 128))

for x in range(RESTFRAMES): 
    WAVEDATA += chr(128)

p = PyAudio()
stream = p.open(
    format=p.get_format_from_width(1),
    channels=1,
    rate=BITRATE,
    output=True,
    )

stream.write(WAVEDATA)
stream.write(WAVEDATA)
time.sleep(0.7)

for x in mcodextend:
    if x == "·":
        stream.write(WAVEDATA)
    elif x == "-":
        time.sleep(0.175)
    else:
        time.sleep(0.35)

stream.stop_stream()
stream.close()
p.terminate()