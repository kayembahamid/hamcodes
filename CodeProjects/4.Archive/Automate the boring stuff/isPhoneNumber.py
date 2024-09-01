def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

# print('415-555-4242 is a phone number:')
# print(isPhoneNumber('414-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))

message = 'Call me at 415-555-1011 tomorrow 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My nnumber is 415-555-4242.')
print('phone number found:' + mo.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My nnumber is 415-555-4242.')
mo.group()   # return the entire match
mo.group(0)  # same as empty
mo.group(1)  # return the first group
mo.group(2)  # return the second group
mo.groups()  # return all the group at once with the plural
print(mo.group())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()
mo2 = heroRegex.search('Tina fey and Batman.')
mo2.group()

print(mo1.group())
print(mo2.group())















