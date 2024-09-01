import shelve

from shelves import shelves


def custom_strip(input_string, characters=None):
    # if characters are not specified, strip whitespace from the beginning and end
    if characters is None:
        return input_string.strip()

    # if the characters are specified, remove them from the begining and end
    # using str.lstrip() and str.rstrip() methods
    left_stripped = input_string.lstrip(characters)
    stripped_string = left_stripped.rstrip(characters)
    return stripped_string

# Example usage
input_string = "  Hello, World!   "
characters_to_strip = "  !"
result = custom_strip(input_string, characters_to_strip)
print("stripped string:", result)

import os
os.path.join('usr', 'bin', 'spam')

myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for filename in myFiles:
    print(os.path.join('/root/usr/macbook', filename))

os.getcwd()

baconFile = open('bacon.txt', 'w')
baconFile.write('Hello world!\n')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is not a vegetable.')
baconFile.close()
baconFile = open('bacon.txt')
content = baconFile.read()
baconFile.close()
print(content)

import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()


