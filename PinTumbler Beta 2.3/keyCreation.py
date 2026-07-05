# PinTumbler Beta 2.2

import encryption
import decryption


def createKey(textInput, keyInput, selection):

    # This key creation function works by:
    #   1. Converting every character of the key input into an ascii number.
    #   2. Adding all of those ascii numbers together to make the key number.
    #   3. Sending the data to the correct function based on the user selection.

    # Get the length of the main menu text input.
    keyLength = len(keyInput)

    # Initialize the key.
    key = 0

    # For the length of the main menu key input.
    for i in range(keyLength):

        # Converts the current character into an ascii number.
        currentAscii = ord(keyInput[i])

        # Add the current ascii number to the key number
        key += currentAscii

    print("[keyCreation Line 29] The key has been calculated to", key)
    print("[keyCreation Line 30] The textInput is", textInput)
    print("[keyCreation Line 31] The selection is", selection)


    # Choose the next function based on the selection.
    if selection.find("Encryption") != -1: # Use find instead of == because == doesn't work.

        # After the key has been created, use it to encrypt the text.
        encryptedText = encryption.encryptText(textInput, key)

        return encryptedText
    
    elif selection.find("Decryption") != -1:
        
        decryptedText = decryption.decryptText(textInput, key)

        return decryptedText
    
