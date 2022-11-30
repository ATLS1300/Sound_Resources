"""
soundResponsive Animation Example

Uses soundResponse library to update shape features. Can also be used for
position, too!

Uncomment line 98 to see frequency animation.

========================
||    REQUIREMENTS    ||
========================

1. Install pydub & simpleaudio. In VS terminal type: 
    
    pip install pydub
    
    
2. In the same folder (select the folder in VS Code, too):
    - tech.wav
    - soundResponse.py    
     
"""

import soundResponse as SR
import pygame
pygame.init()


w = 600 # width of panel
h = 600 # height of panel
win = pygame.display.set_mode((w,h))

class SRcirc:
    ''' Bubble class that responds to music!'''
    def __init__(self,x,y,rad=50,color=[255,255,255]):
        self.x = x
        self.y = y
        self.orig_rad = rad
        self.rad = rad
        self.color = color
        self.rect = pygame.draw.circle(win,self.color,(self.x,self.y),rad)
        
    def show(self):
        self.rect = pygame.draw.circle(win,self.color,(self.x,self.y),self.rad)

    def shapesize(self,val):
        self.rad =self.orig_rad+val # adds changing val to fixed radius (easier to see)
        self.show()
        
    def setColor(self,color):
        self.color = pygame.Color(color) # will process any input: HEX (string), tuple, RGB
        self.show()
        
        
# create a Controller object. Pass your sound file name in as a str.
class Animation:
    '''Manager class for animation.'''
    def __init__(self):
        self.running = True

    def stop(self):
        '''callback function that stops animation while it's running'''
        self.running = False

    def run(self):
        '''Same as main() method'''
        
        music = SR.Ctrlr('tech.wav') # create controller object
        fCirc = SRcirc(w/2-100,h/2,100,[100,100,100]) #bigger gray SRcirc object to respond to frequency
        aCirc = SRcirc(w/2+100,h/2) # SRcirc object to respond to amplitude

        clock = pygame.time.Clock()   
            
        music.start() # start song
        
        while self.running:
            win.fill((0,0,0))
            
            # === USING AMP VALUES TO CHANGE SIZE & COLOR ===
            #getCurrAmp returns amplitude and the sample index (where the animation is in the song)
            amp, _ = music.getCurrAmp() #work only with the first value returned, the amplitude
            amp /= 1000  # scale down so we can actually see it
            print(f"Amp: {amp}")
            
            # channge shapesize
            aCirc.shapesize(amp) 
        
            # changing two visuals with 1 sound feature (amp or freq) makes it easier to notice
            if amp > 3:
                aCirc.setColor('lavender') #turn light color if really loud.
            else:
                aCirc.setColor('yellow')
        
            # === USING FREQ VALUES TO CHANGE COLOR ===
            #getCurrFreq returns the frequency (pitch) and the sample index (where the animation is in the song)
            freq, _ = music.getCurrFreq() #work only with the first value returned, the amplitude
                # bass: 20-150, mids: 150-1500, highs: >1500
            
            #COMMENT OUT TO SHOW:
            fCirc = False # to show one feature at a time.
            
            print(f"Freq: {freq}")
            
            if freq<500:
                'bass'
                fCirc.setColor("purple")
            # elif 150<=freq<1500:
            #     'mids'
            #     fCirc.setColor("purple")
            else:
                'highs'
                fCirc.setColor("pink")
            
            pygame.display.update()
            clock.tick(80) # higher frame rates (up to 120) make cleaner animations
            
            # === STOPPING === 
            # when the song ends, amp = -1 (whole number amp values are rare)
            if amp ==-1:
                self.stop() # will stop loop
             
            # stop with exit (will stop loop)   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
        pygame.quit()
        
                    
Animation().run()