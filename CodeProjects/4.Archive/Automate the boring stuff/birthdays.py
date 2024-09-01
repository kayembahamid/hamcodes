birthdays = {'Joy': 'Jan 05', 'Mitch': 'sept 08', 'cyberTron': 'Dec 26'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('what is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('birthday database updated.')