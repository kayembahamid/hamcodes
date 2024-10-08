# Transposition cipher Decryption
# http://inventwithpython.com/hacking (BSD licensed)

import math, pyperclip

def main():
    myMessage = "Bmmsrl(s)dpnaua!toeboo'ktn(s)uknrwos.(s)yaregonr(s)w(s)nd,tu(s)(s)oiady(s)hgtRwt(s)(s)(s)A(s)hhanhhasthtev(s)(s)e(s)t(s)e(s)(s)eo"
    myKey = 9

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | (called "pipe"character) after it in case
    # there are spaces at the end of the decrypted message
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings.First, we need to calculate a few values.

    # The number of "columns"in our transposition grid:
    numOfColumns = math.ceil(len(message) / key)
    # The number of "rows"in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column"of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The col and row variables point to where in the grid the text
    # character in the encrypted message will go.
    col = 0
    row = 0

    for symbol in message:
        plaintext[col] += symbol
        col += 1  # point to next column

        # if there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row.
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# if transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
        main()

