#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 13:35:03 2021

@author: sazamore

Example of using pygame to create sound in scripts.
For more information about pygame mixer and sound operation, check out
the docs!
https://www.pygame.org/docs/ref/music.html


HOW TO USE THIS CODE:

    INSTALL PYGAME.
    1. go to command line interface
    2. type in:
    pip install pygame
    3. press enter
    
    USE THE CODE:
    1. You can run it! And see how it works!
    2. You can import it, and use the methods inside the library!
        from pySound import Sound
        sound = Sound('oof.wav')
        sound.playFX() # plays sound effect
        
        OR
        from pySound import Sound
        sound = Sound('oof.wav','tech.wav')
        sound.playFX() # plays sound effect
        sound.playBG() # plays background music
        
    3. YOU MUST create a folder called sound for your sound files.

Modified from https://opensource.com/article/20/9/add-sound-python-game
"""
import pygame, os

# initialize pygame mixer for sound use
pygame.init()
pygame.font.init()
pygame.mixer.init()

class Sound:
    def __init__(self, soundfile, bgSoundfile=None):
        '''soundfile can be list of sounds or single sound!
        This version only supports 1 background soundfile. I may update it later.'''
        self.soundfile = soundfile
        self.bgSoundfile = bgSoundfile
        
        if type(self.soundfile) == list:
            self.sound = []
            for sound in range(len(self.soundfile)):
                self.sound.append(pygame.mixer.Sound(os.path.join('sound',sound)))
        else: 
            self.sound = pygame.mixer.Sound(os.path.join('sound',self.soundfile))
        
        if self.bgSoundfile:
            self.music = pygame.mixer.music.load(os.path.join('sound', self.bgSoundfile))
    
    def playFX(self):
        '''Plays sound effects. Use with clickback functions!'''
        pygame.mixer.Sound.play(self.sound)
        
    def playBG(self):
        '''Plays background music. Use at the start of your game (run function)!'''
        pygame.mixer.music.play(-1)
        
    def stopBG(self):
        '''Stops background music.'''
        pygame.mixer.music.stop()
        
    def pauseBG(self):
        '''Stops background music and remember sound location'''
        pygame.mixer.music.pause()
        
    def unmpauseBG(self):
        '''Resumes background music play at paaused location'''
        pygame.mixer.music.unpause


if __name__=='__main__':
    sound = Sound('oof.wav')
    sound.playFX()
