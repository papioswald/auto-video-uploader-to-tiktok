import os
from clicknium import clicknium as cc, locator,ui
import time
import mouse
from pynput.keyboard import Key, Controller

# Imports
keyboard = Controller()


def type(word):
    time.sleep(1)
    keyboard.type(word)

# Variables and function for typing description of video


tab = cc.chrome.open(url="www.tiktok.com/upload?lang=en")
time.sleep(5)
ui(locator.tiktok.button_select_file).click()
ui(locator.tiktok.edit_file_name).set_text(r"D:\111111\coding\tiktok\fyp.mp4")
ui(locator.tiktok.button_open).click(by='mouse-emulation')
#Opens browser and finds video
time.sleep(6)
mouse.move(1080,514)
mouse.click()
keyboard.press(Key.backspace)
time.sleep(0.5)
keyboard.press(Key.backspace)
time.sleep(0.5)
keyboard.press(Key.backspace)
time.sleep(0.5)
keyboard.press(Key.backspace)
time.sleep(0.5)
#Removes all text so that it will appear as [tiktok i am human i swear https://discord.gg/xy6HWKH9 #fyp #goofy #rizzgod #fyp #comedyking] instead of [fyptiktok i am human i swear https://discord.gg/xy6HWKH9 #fyp #goofy #rizzgod #fyp #comedyking]
type("tiktok i am human i swear https://discord.gg/xy6HWKH9 #fyp #goofy #rizzgod #fyp #comedyking")
time.sleep(5)
mouse.wheel(4)
tab.find_element(locator.tiktok.button_post).click()
#Posts video and adds description
time.sleep(10)
tab.close()
#Exits out of chrome