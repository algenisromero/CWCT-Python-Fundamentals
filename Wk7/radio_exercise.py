##########################################################################
# Program Name: radio_exercise.py
#
# Author: Algenis Romero
# Course: Introduction to Python for Cybersecurity (CWCT-140)
# Assignment: M03 - Programming assignment
# Date: September 28, 2023,
#
# Description:
# The program contains code which references a Radio class that you will design.
##########################################################################

from tkinter import *
from PIL import ImageTk,Image  

#Define "Radio" class here
class Radio:
    # - constructor takes initial volume and frequency
    def __init__(self, volume, frequency):
        self._volume = volume
        self._frequency = frequency
    # - VolumeUp method increases volume by 1 to limit of 10
    def VolumeUp(self):
        if self._volume < 10:
            self._volume += 1
    # - VolumeDown method decreases volume by 1 to limit of 0
    def VolumeDown(self):
        if self._volume > 1:
            self._volume -= 1
    # - FrequencyUp method increases frequency by 0.1 to limit of 108.0
    def FrequencyUp(self):
        if self._frequency < 107.9:
            self._frequency += 0.1
    # - FrequencyDown method decreases frequency by 0.1 to limit of 88.0
    def FrequencyDown(self):
        if self._frequency > 88.1:
            self._frequency -= 0.1
    # - __str__ method returns volume and frequency as illustrated below:
    def __str__(self):
    # -   return "Volume: " + str(self._volume) + "\n\nFrequency: " + str(round(self._frequency, 1))
        return "Volume: " + str(self._volume) + "\n\nFrequency: " + str(round(self._frequency, 1))

#Define the path to the radio image
radioimage = "radio.png"

#Unit Test for Digital Radio
#No need to modify anything below here

def volume_up(myRadio):
    myRadio.VolumeUp()
    displaylabel.config(text = myRadio)

def volume_down(myRadio):
    myRadio.VolumeDown()
    displaylabel.config(text = myRadio)

def frequency_up(myRadio):
    myRadio.FrequencyUp()
    displaylabel.config(text = myRadio)

def frequency_down(myRadio):
    myRadio.FrequencyDown()
    displaylabel.config(text = myRadio)

#Main program
try:
    myRadio = Radio(5, 101.5)
except Exception as e:
    print(e)

root = Tk()  
canvas = Canvas(root, width = 616, height = 600)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(radioimage))  
canvas.create_image(0, 0, anchor=NW, image=img)
try: 
    displaylabel = Label(canvas, text=myRadio, background="black", foreground="lightgreen", font=("Helvetica", 24))
except:
    displaylabel = Label(canvas, text="Radio class missing", background="black", foreground="lightgreen", font=("Helvetica", 24))
displaylabel.place(x=106,y=214, width=406, height=178)
volumelabel = Label(canvas, text="Volume", font=("Helvetica", 18))
volumelabel.place(x=125,y=480)
volupbtn = Button(root, text="Up", font=("Helvetica", 14), command=lambda:volume_up(myRadio))
volupbtn.place(x=80,y=478)
voldownbtn = Button(root, text="Down", font=("Helvetica", 14), command=lambda:volume_down(myRadio))
voldownbtn.place(x=215,y=478)
tunelabel = Label(canvas, text="Tune", font=("Helvetica", 18))
tunelabel.place(x=400,y=480)
tuneupbtn = Button(root, text="Up", font=("Helvetica", 14), command=lambda:frequency_up(myRadio))
tuneupbtn.place(x=350,y=478)
tundownbtn = Button(root, text="Down", font=("Helvetica", 14), command=lambda:frequency_down(myRadio))
tundownbtn.place(x=465,y=478)
closebtn = Button(root, text="Close", font=("Helvetica", 14), command=root.destroy)
closebtn.place(x=280, y=550)
root.mainloop() 