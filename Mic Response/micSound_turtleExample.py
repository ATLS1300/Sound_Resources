import micSound
import math
import turtle
    
def instruct():
    turtle.color("white")
    turtle.ht()
    
    turtle.up()
    turtle.goto(0,100)
    turtle.write("Make noise!", font=("Verdana",20, "bold"))
    turtle.home()
    turtle.down()
    turtle.update()

def parrot(theta,scale=50):
    # equations from https://www.flerlagetwins.com/2018/04/parrot.html
    # theta = math.radians(t)
    turtle.color("aliceblue")

    if turtle.xcor()==0:
        turtle.up()
    else:
        turtle.down()
        
    for i in range(10):
        x = (3*theta/20000)+(math.cos(37*math.pi*theta/10000))**6 * math.sin((theta/10000)**7*(3*math.pi/5))+(9/7)*(math.cos(37*math.pi*theta/10000))**16*(math.cos(math.pi*theta/20000))**12 * math.sin(math.pi*theta/10000)

        y = (-5/4)*(math.cos(37*math.pi * theta/10000))**6 * math.cos((theta/10000)**7 * (3*math.pi/5))*(1+3*(math.cos(math.pi*theta/20000)*math.cos(3*math.pi*theta/20000))**8)+(2/3)*(math.cos(3*math.pi*theta/200000)*math.cos(9*math.pi*theta/200000)* math.cos(9*math.pi*theta/100000))**12
        turtle.width(4)
        turtle.goto(x*scale, y*scale)
        theta += 20
    turtle.update()
    if theta >= 10800:
        theta = 10800 # stop the animation
    return theta
        
def main():     
    # LIBRARY USE
    micSound.makeStream()
    threshold = 0.3 # threshold forr doing sound-related activities. Tweak this value!
    
    # turtle stuff
    turtle.Screen().bgcolor('darkmagenta')
    instruct() # draws instructions on screen
    running = True
    f=-10800

    while running:
        chunk = micSound.sample(micSound.stream,10000) # gets amplitude from microphone  stream

        if max(abs(chunk[0])) >= threshold:
            # if the absolute value of loudness is greater than a threshold...
            # lower threshold valuues => detect quieter sounds. 
            # 0.3 good for clapping, blowing on mic, snapping
            
            f = parrot(f)
            if f >= 10800:
                turtle.ht()
                turtle.getscreen().bgcolor("darkslateblue")
                running = False
    turtle.mainloop()
    
    micSound.cleanup(micSound.stream) # Always call at the end!
    
main()