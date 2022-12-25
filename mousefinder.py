from pynput import *
def get_coords(x, y):
    print(format((x,y)))

with mouse.Listener(on_move=get_coords) as listen:
    listen.join()

#Used for finding mouse coordinates for clicking and typing description for tiktok video
