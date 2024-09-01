# Transposition Cipher Encrypt/Decrypt File
# http://inventwithpython.com/hacking (BSD Licensed)

import time, os, sys, transpositionEncrypt, transpositionDecrypt

def main():
    inputFilename = 'frankenstein.txt'
    # BE CAREFUL! If with the outputFilename name already exists,
    # this program will overwrite that file.
    outputFilename = 'frankenstein.encrypted.txt'
    myKey = 10
    myMode = 'encrypt'  # set to 'encrypt'or 'decrypt'

    # If the input file does not exists, then the program terminates early.
    if not os.path.exists(inputFilename):
        print('The file %s does not exist. Quitting...'% (inputFilename))
        sys.exit()

    # if the output file already exists, give thee user a chance to quit.
    if os.path.exists(outputFilename):
        print('This will overwrite the file %s. (c)ontinue or (Q)uit?'% (outputFilename))
        response = input('>')
        if not response.lower().startwith('c'):
            sys.exit()

    # Read in the message from the input file
    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print('%sing...' % (myMode.title()))

    # Measure how long the encryption/decryption takes.
    startTime = time.time()
    if myMode == 'encrypt':
        translated = transpositionEncrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), totalTime))

    # Write out the translated message to the output file.
    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters).' % (myMode, inputFilename,len(content)))
    print('%sed file kis %s.' % (myMode.title(), outputFilename))

# if transpositionCipherFile.py is run (instead of the imported aas a module)
# call the main() function.
if __name__ == '__main__':
    main()

