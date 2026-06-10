# PinTumbler Beta 2.1

def decryptText(textInput, key):

    # This decryption function works by:
    #   1. Searching the text input (convert to int) for a number that is divisible by the key.
    #   2. Divide the character by the key.
    #   3. Convert the new number (ascii) into a character.
    #   4. Append that character to a string.
    #   5. Add the difference between start and i to start (moves the beginning of the substring to exclude a previously decrypted char).

    # Get the length of the main menu text input.
    textInputLength = len(textInput)

    # Initialize the start variable where the substring of the input begins.
    start = 0

    # Initialize the decrypted text.
    decryptedText = ""

    print(textInput + " is textInput at line 124.")

    for i in range(textInputLength + 1):

        # The try and except is in case there is no value in the substring.
        try:

            # Turn the text input into a substring to search for a char.
            textInputSub = textInput[start:i]

            print(textInputSub + " is textInputSub at line 134.")

            # Turn the text input sub into an int.
            textInputSubInt = int(textInputSub)

            # If the text input sub is divisible by the key.
            if textInputSubInt % key == 0:

                # If the next substring is not divisible by the key.
                # This is to prevent dividing too early when a number has many zeros, and is therefore divisible by the key when not completely selected.
                # The or condition is the prevent cutting off the last digit because there is no i + 1 char (because the end has been reached).
                if int(textInput[start:(i + 1)]) % key != 0 or i == (textInputLength - 1):
                
                    # Divide the text input sub by the key to get the ascii number.
                    currentAscii = textInputSubInt / key

                    # Turn the ascii number into a character.
                    # It is casted into an int because there will be a .0 at the end of the number, but floats cannot be converted to chars.
                    currentChar = chr(int(currentAscii))

                    # Append the decrypted character to the decrypted text.
                    decryptedText += currentChar

                    # Update the start variable with the new difference.
                    difference = i - start
                    start += difference

                    print("The try block in the encryptText function has successfully been executed!")
                    print("The char that was decrypted is " + currentChar)
                    print("The start variable is ")
                    print(start)
                    print("The i variable is ")
                    print(i)
        
        except:
            print("An error has occurred at the try block in the encryptText function.")

    return decryptedText