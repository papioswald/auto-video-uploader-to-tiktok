import os
import random

videodir = os.listdir("media/videos")
imagedir = os.listdir("media/images")
audiodir = os.listdir("media/audio")


random1 = ("media/videos/" + random.choice(videodir))
random2 = ("media/images/" + random.choice(imagedir))
random3 = ("media/images/" + random.choice(imagedir))
random4 = ("media/audio/" + random.choice(audiodir))
#Video variables

