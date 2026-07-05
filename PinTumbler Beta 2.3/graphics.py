# PinTumbler Beta 2.2

# Grid dimension is 5x5

import main
import tkinter
from tkinter import *
from tkinter import ttk
import keyCreation

# Initialize variables that need to be accessed by multiple functions.
window = Tk()
frame = ttk.Frame()


window.resizable(False, False)

selection = ""


# These variables need to be accessed by the erase function, so they must be declared outside of any other functions.
textEntryLabel = ttk.Label(window, text = "Your text:", font = ("Times New Roman", 12, "bold"))
passwordEntryLabel = ttk.Label(window, text = "Your password:", font = ("Times New Roman", 12, "bold"))
titleLabel = ttk.Label(window, text = "PinTumbler", font = ("Times New Roman", 50, "bold"))
titleDescriptionLabel = ttk.Label(window, text = "Password manager and security utility.", font = ("Times New Roman", 15, "bold"))
softwareVersionLabel = ttk.Label(window, text = "Beta 2.2", font = ("Times New Roman", 12, "bold"))
resultLabel = ttk.Label(window, font = ("Times New Roman", 12, "bold"))
selectionLabel = ttk.Label(window, text = selection, font = ("Times New Roman", 50, "bold"))

textEntry = ttk.Entry(window)
passwordEntry = ttk.Entry(window)

encrypterButton = ttk.Button(window, text = "Encrypter", command = lambda:keyCreationGraphics("Encryption"))
decrypterButton = ttk.Button(window, text = "Decrypter", command = lambda:keyCreationGraphics("Decryption"))
keyCreationEnterButton = ttk.Button(window, text = "Continue", command = lambda:sendKeyCreationInstructions(textEntry.get(), passwordEntry.get(), selection))

rowSpacer = ttk.Label(window, text = "")
rowSpacer2 = ttk.Label(window, text = "")

widgets = [
    textEntryLabel,
    passwordEntryLabel,
    titleLabel,
    titleDescriptionLabel,
    softwareVersionLabel,
    resultLabel,
    selectionLabel,
    textEntry,
    passwordEntry,
    encrypterButton,
    decrypterButton,
    keyCreationEnterButton,
    rowSpacer,
    rowSpacer2
]

# This function is just to test buttons.
def test():

    print("Hello world!")

# This function runs the key creation UI.
def keyCreationGraphics(selection):

    # This key creation UI function works by:
    #   1.

    eraseWidgets() # Destroys the widgets

    selectionLabel = ttk.Label(window, text = selection, font = ("Times New Roman", 50, "bold")) # Re-initialize so the selection variable is refreshed
    selectionLabel.grid(
        column = 0, row = 0,
        columnspan = 3,
        pady = 10
    )

    # Text entry label.
    textEntryLabel.grid(
        column = 0, row = 1,
        sticky = E,
        padx = 10, pady = 10
    )

    textEntry.grid(
        column = 1, row = 1,
        sticky = W,
        padx = 10, pady = 10
    )

    passwordEntryLabel.grid(
        column = 3, row = 1,
        sticky = E,
        padx = 10, pady = 10
    )

    passwordEntry.grid(
        column = 4, row = 1,
        sticky = W,
        padx = 10, pady = 10
    )

    rowSpacer.grid(
        column = 0, row = 2,
        columnspan = 5
    )

    # Initialize the button again so the selection variable will be defined.
    keyCreationEnterButton = ttk.Button(window, text = "Continue", command = lambda:sendKeyCreationInstructions(textEntry.get(), passwordEntry.get(), selection))
    keyCreationEnterButton.grid(
        column = 2, row = 3,
        sticky = NSEW
    )

    softwareVersionLabel.grid(
        column = 4, row = 4,
        columnspan = 2,
        sticky = SE,
    )

def sendKeyCreationInstructions(textInput, keyInput, selection):

    # This function sends the instructions to the keyCreation class to execute.

    eraseWidgets()

    result = keyCreation.createKey(textInput, keyInput, selection)

    resultLabel = ttk.Label(text = result)
    resultLabel.grid()

# Make the result visible.
    
    print("The result is ", result)



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

    # Set the position of the frame and stick it to the sides.
    frame.grid()

def initializeWidgets():

    # This widget initialization function works by:
    #   1. Setting every widget in order from left to right, top to bottom.


    # Title label.
    titleLabel.grid(
        column = 0, row = 0,
        columnspan = 3,
        pady = 10
    )

    # Encrypter button.
    # This button launches the main menu.
    encrypterButton.grid(
        column = 1, row = 1,
        columnspan = 1, rowspan = 1,
        sticky = NS,
        pady = 10
    )

    # Decrypter button.
    # This button launches the main menu.
    decrypterButton.grid(
        column = 3, row = 1,
        columnspan = 1, rowspan = 1,
        sticky = NS,
        pady = 10
    )

    rowSpacer.grid(
        column = 0, row = 2,
        columnspan = 5
    )

    rowSpacer2.grid(
        column = 0, row = 3,
        columnspan = 5,
        pady = 10
    )

    # Software version label.
    softwareVersionLabel.grid(
        column = 4, row = 4,
        columnspan = 2,
        sticky = SE,
    )

    
def eraseWidgets():

    x = 0

    for i in widgets:
        widgets[x].grid_remove()
        x += 1

def initializeGraphics():

    # This graphics running function works by:
    #   1. Running the other graphics functions.
    #   2. Using mainloop to run and update graphics.

    initializeFrame()
    initializeWidgets()
    

    # Runs and updates the graphics.
    window.mainloop()

    
