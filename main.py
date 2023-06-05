import os
import pygame
from tkinter import *
from tkinter.filedialog import askdirectory
from mutagen.id3 import ID3

root = Tk()
root.minsize(300,300)

listofsongs = []
realnames = []

v = StringVar()
songlabel = Label(root,textvariable = v,width = 35)

index = 0

def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()

directorychooser()

def updatelabel():
    global index
    global songname
    v.set(realnames[index])
    #return songname



def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def unpausesong(event):
    pygame.mixer.music.unpause()
    #pausebutton.config(text="pause song")
    v.set("Song unpasued")
    #return songname

def pausesong(event):
    pygame.mixer.music.pause()
    v.set("Song Paused")
    #pausebutton.config(text="unpasue song")
    #return songname

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname


label = Label(root,text='Music Player')
label.pack()

listbox = Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()


nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()

pausebutton = Button(root, text= 'Pause Song')
pausebutton.pack()

unpausebutton = Button(root, text= 'Unpause Song')
unpausebutton.pack()

stopbutton = Button(root,text='Stop Music')
stopbutton.pack()


nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
pausebutton.bind("<Button-1>",pausesong)
unpausebutton.bind("<Button-1>",unpausesong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()
root.mainloop() 