from subprocess import call
from datetime import datetime
import time
import os
import notifypy
import logging
import globalvars
#Imports

now = datetime.now()
current_time = now.strftime("%H:%M")

hour = int(16)
minutes = int(46)

notif = notifypy.Notify()
notif1 = notifypy.Notify()

notif.title = "info"
notif.message = f"the time is {current_time}, the code will start at {hour}:{minutes}"
notif.icon = "bin/IMG_2230.png"
notif.application_name = "tiktok bot"
notif.audio = "bin/notification.wav"
notif.send()


notif1.title = "info"
notif1.message = "process started"
notif1.icon = "bin/IMG_2230.png"
notif1.application_name = "tiktok bot"
notif1.audio = "bin/notification.wav"

#Variables and notification configs

print("dont close this window, the time is:",current_time)

def open_video_creator():
    call(["python","edit.py"])

def upload_video():
    call(["python","uploader.py"])

#Function to open scripts

while True:
    if hour == datetime.now().hour and minutes==datetime.now().minute:
        print("works")
        notif1.send()
        open_video_creator()
        upload_video()
        #Runs script and waits 60 seconds to delete fin
        time.sleep(60)
        print("removin")
        os.remove(globalvars.random1)
        os.remove(globalvars.random2)
        os.remove(globalvars.random3)
        os.remove(globalvars.random4)
        print("removed")
        #Removes media
        break

time.sleep(5)