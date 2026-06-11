# PinTumbler Beta 2.2

# Things to improve: 
#   1. Get the decryption to decrypt the last character successfully.
#   2. Make the createKey function only return the key.
#   3. The condition of the if in the decrypter that makes sure that if a number has 0000s at the end it wont divide too soon might not work because it doesn't know how many extra zeros there will be.
#      Zeros cannot be at the beginning of number, take that into account.

import keyCreation
import graphics

def launchMainMenu():

    # This main menu function works by:
    #   1. Getting the function (encryption or decryption), text, and key the user would like to use.
    #   2. Calling the function the user requested.

    # Prompt the user to select encryption or decryption.
    print("Would you like to encrypt or decrypt your text? ")
    selection = input()

    # Prompt the user to enter their text.
    print("Please enter your text: ")
    textInput = input()

    # Prompt the user to enter their key.
    print("Please enter your key: ")
    keyInput = input()

    # Call the function desired by the user.
    if selection == "encrypt":

        # Call the createKey function for encryption.
        encryptedText = keyCreation.createKey(textInput, keyInput, selection)

        print("The encrypted text is " + encryptedText)

    elif selection == "decrypt":

        # Call the createKey function for decryption.
        decryptedText = keyCreation.createKey(textInput, keyInput, selection)

        print("The decrypted text is: " + decryptedText)

    else:
        print("Invalid input, please try again.")
        launchMainMenu()

graphics.runGraphics()