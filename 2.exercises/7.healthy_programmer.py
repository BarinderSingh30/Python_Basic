# -------------------------------------------HEALTHY PROGRAMMER--------------------------------------
"""
9 AM TO 5 PM
3.5 litre water reminder using audio
eyes excercise after 30 minutes
physical excercise after 45 minutes

record time of their excercise

use pygame module to play audio
"""
from pygame import mixer
import time
import keyboard

def play_music(s):

    if s=='water':
        mixer.init()
        mixer.music.load('water.mp3')
        mixer.music.set_volume(0.7)
        mixer.music.play(loops=-1)
    elif s=='eye':
        mixer.init()
        mixer.music.load('eyes.mp3')
        mixer.music.set_volume(0.7)
        mixer.music.play(loops=-1)
    elif s=='physical':
        mixer.init()
        mixer.music.load('physical.mp3')
        mixer.music.set_volume(0.7)
        mixer.music.play(loops=-1)
    return


def log_time(s):

    f=open('healthyprogrammer.txt','a')

    localtime = time.asctime(time.localtime(time.time()))

    if s=='water':
        f.write(f'250 ml water at : {localtime}\n')
    elif s=='eye':
        f.write(f'eye excercise at : {localtime}\n')
    elif s=='physical':
        f.write(f'physical activity  at : {localtime}\n')
    
    f.close()
    return





initialw = time.time()
initiale = time.time()
initialp = time.time()

if __name__=='__main__':
    while True:
        t=time.time()

        if t-initialw >2400:
            play_music('water')
            s=input('type done to stop the music')
            mixer.music.stop()
            log_time('water')
            initialw = time.time()

        if t-initiale >1800:
            play_music('eye')
            s=input('type done to stop the music')
            mixer.music.stop()
            log_time('eye')
            initiale = time.time()

        if t-initialp >2700:
            play_music('physical')
            s=input('type done to stop the music')
            mixer.music.stop()
            log_time('physical')

            initialp = time.time()

        if keyboard.is_pressed('p'):
            break