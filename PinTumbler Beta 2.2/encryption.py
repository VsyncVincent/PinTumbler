# PinTumbler Beta 2.2

def encryptText(textInput, key):

    # This encryption function works by:
    #   1. Converting every character into an ascii number and multiplying it by the key.
    #   2. Appending the new number onto the end of a string.

    # Get the length of the main menu text input.
    textInputLength = len(textInput)

    # Initialize the encrypted text.
    encryptedText = ""

    # For the length of the main menu text input.
    for i in range (textInputLength):

        # Converts the current character into an ascii number.
        currentAscii = ord(textInput[i])

        # Multiply the current ascii number by the key, thus encrypting it.
        encryptedAsciiNumber = currentAscii * key

        # This adds the encrypter character into the encrypted text string.
        encryptedText += str(encryptedAsciiNumber)

    return encryptedText