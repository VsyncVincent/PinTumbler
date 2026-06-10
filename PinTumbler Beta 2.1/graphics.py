# PinTumbler Beta 2.1

import main
import tkinter
from tkinter import *
from tkinter import ttk

# Initialize variables that need to be accessed by multiple functions.
window = Tk()
frame = ttk.Frame()

def initializeFrame():

    # This frame initialization function works by:
    #   1. Creating the window.
    #   2. Creating the frame.
    
    # Set the title of the window.
    window.title("Hello")

    # Set the size of the frame.
    frame['width'] = 1280
    frame['height'] = 720

    # Set the position of the frame and stick it to the sides.
    frame.grid(column = 0, row = 0, sticky = (N, W, E, S))

def initializeWidgets():

    # This widget initialization function works by:
    #   1. Setting every widget in order from left to right, top to bottom.

    # Title label.
    titleLabel = ttk.Label(window, text = "PinTumbler", font = ("Times New Roman", 50, "bold"))
    titleLabel.grid(column = 0, row = 0, sticky = (N))

    # Title description label.
    titleDescriptionLabel = ttk.Label(window, text = "Password manager and security utility.", font = ("Times New Roman", 15, "bold"))
    titleDescriptionLabel.grid(column = 0, row = 1, sticky = (N))

    # Encrypter button.
    encrypterButton = ttk.Button(window, text = "Encrypter", command = )
    encrypterButton.grid(column = 0, row = 3)

    # Software version label.
    softwareVersionLabel = ttk.Label(window, text = "Beta 2.1", font = ("Times New Roman", 12, "bold"))
    softwareVersionLabel.grid(column = 0, row = 10, sticky = (S, E))

def runGraphics():

    # This graphics running function works by:
    #   1. Running the other graphics functions.
    #   2. Using mainloop to run and update graphics.

    initializeFrame()
    initializeWidgets()

    # Runs and updates the graphics.
    window.mainloop()

runGraphics()