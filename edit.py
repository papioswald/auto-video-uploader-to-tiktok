import os
import random
import moviepy.editor as mp
from moviepy.editor import *
import time
import globalvars
import cv2


cam = cv2.VideoCapture(globalvars.random1)
fps = cam.get(cv2.CAP_PROP_FPS)




media = []
clip1 = VideoFileClip(globalvars.random1).set_fps(fps + 90).set_duration(2) #I dont think the (fps + 90) part is doing anything
clip2 = ImageClip(globalvars.random2).fx(vfx.fadein, 0.3).set_duration(2)
clip3 = ImageClip(globalvars.random3).fx(vfx.fadein, 0.3).set_duration(3)
audio = AudioFileClip(globalvars.random4)
audio = audio.set_duration(7)
media.append(clip1)
media.append(clip2)
media.append(clip3)
#Gathers clips for video
video = concatenate_videoclips(media, method='compose')
new_audio = mp.CompositeAudioClip([audio])
video.audio = new_audio


video.write_videofile(filename="fyp.mp4", fps=24, remove_temp=True, codec="libx264", audio_codec="aac")
#Creates video as mp4 for upload