# PinTumbler Beta 2.2

import main
import tkinter
from tkinter import *
from tkinter import ttk

# Initialize variables that need to be accessed by multiple functions.
window = Tk()
frame = ttk.Frame()

# This function is just to test buttons.
def test():

    print("Hello world!")

# This function runs the key creation UI.
def keyCreationGraphics(selection):

    # This key creation UI function works by:
    #   1.

    # Text entry label.
    textEntryLabel = ttk.Label(window, text = "Your text:", font = ("Times New Roman", 12, "bold"))
    textEntryLabel.grid(column = 0, row = 4, sticky = (W))

    # Text entry.
    textEntry = ttk.Entry(window)
    textEntry.grid(column = 2, row = 4, sticky = (E))

    # Password entry label.
    passwordEntryLabel = ttk.Label(window, text = "Your password:", font = ("Times New Roman", 12, "bold"))
    passwordEntryLabel.grid(column = 0, row = 5, sticky = (W))

    # Password entry.
    passwordEntry = ttk.Entry(window)
    passwordEntry.grid(column = 2, row = 5, sticky = (E))

    print(selection)

    

# This function runs the encryption UI.
#def encryptionGraphics():

# This function runs the decryption UI.
#def decryptionGraphics():

def initializeFrame():

    # This frame initialization function works by:
    #   1. Creating the window.
    #   2. Creating the frame.
    
    # Set the title of the window.
    window.title("Hello")

    # Set the size of the frame.
    frame['padding'] = 5
    frame['width'] = 600
    frame['height'] = 480

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
    # This button launches the main menu.
    encrypterButton = ttk.Button(window, text = "Encrypter", command = lambda:keyCreationGraphics("encrypt"))
    encrypterButton.grid(column = 0, row = 2, sticky = (W))

    # Decrypter button.
    # This button launches the main menu.
    encrypterButton = ttk.Button(window, text = "Decrypter", command = lambda:keyCreationGraphics("decrypt"))
    encrypterButton.grid(column = 5, row = 2, sticky = (E))

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
