#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 12:10:59 2021

@author: sazamore

Uses sounddevice library to record from laptop microphone.

TO USE: In VS terminal, type:
    pip install sounddevice
    
You will need to allow microphone permissions to get this code to run properly.

Code modified from https://realpython.com/playing-and-recording-sound-python/#recording-audio
and https://www.programcreek.com/python/example/123596/sounddevice.InputStream
"""
import sounddevice as sd
from scipy.io.wavfile import write
import time

def recVoice(dur=3,fs=44100,save=True,countdown=True):
    '''Uses built-in microphone to record. May not work on device without a built
    in mic.
    Arguments: 
        dur (int/float) - duration of time to record
        fs (int) - sample rate of recording. 44100 is recommended.
        save (bool) - determines if recording will be saved to file or not.
        Cannot use sample without saving.
    Returns:
        myrecording - a numpy array of the recorded sample. Good for graphing/interactions'''    
    
    if countdown:
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Go!")
    
    myrecording = sd.rec(int(dur * fs), samplerate=fs, channels=2)
    print('recording...')
    # sd.wait()  # Wait until recording is finished
    
    # print('recording complete.')
    if save:
        write('output.wav', fs, myrecording)  # Save as WAV file 
    return myrecording

stream=None

def makeStream(device=None, soundrate=44100):
    global stream
    if stream is not None:
        stream.close()
        print('recording stopped.')
    stream = sd.InputStream(samplerate=soundrate, channels=1,)
    stream.start()
    
def sample(stream,soundrate=44100,framerate=.3):
    chunk = stream.read(soundrate)
    return chunk

def cleanup(stream):
    if stream is not None:
        print('recording stopped')
        stream.close()
