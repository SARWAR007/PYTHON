birthdays = {'Farhan':'May-22','Faizan':'Nov:21','Ezaan':'Dec:15'}

while True:
    print('Enter a Name:(blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + 'is the birthday of' +name)

    else:
        print('I donot have birthday info for this '+name)
        print('Enter the birthday for ' + name + ' and we will save it')
        bday = input()
        birthdays[bday] = bday
        print('Birthday database updated.' + birthdays[name])
        
