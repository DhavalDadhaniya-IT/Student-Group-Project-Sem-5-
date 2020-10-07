import subprocess
import sys
import os
from gpiozero import Button
from gpiozero import LED
from time import sleep
LOCK = LED(17)
def face():
    returned_text = subprocess.check_output("python3 recognition.py", shell=True, universal_newlines=True)
    a = returned_text
    print("Face Recognized")
    if "dhaval-dadhaniya" in a:
        LOCK.on()
        sleep(2)
        LOCK.off()
        print("Door is Open")
    else:
        print("Unknown Person")
    print(returned_text)
    remember = open('text.txt','w')
    remember.write(returned_text)
    remember.close()

button = Button("GPIO26")
while True:
    if button.is_pressed:
        print("Button is pressed")
        face()
        exit()
