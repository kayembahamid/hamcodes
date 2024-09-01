# Reverse cipher
# encrypt
# message = 'Three can keep a secret, if two of them are dead.'
# decrypt
# message = '.daed era meht fo owt fi ,terces a peek nac eerhT'
message = input('Enter message: ')
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i - 1

print(translated)
