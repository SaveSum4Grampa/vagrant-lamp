import random
pets = {'Kiba':['Fluffy',],'Obi':['a smudge',]}

while True:
    print('Enter the name of a family member: (use "no" to exit)')
    pet = input()
    if pet == 'no':
        break
    elif pet in pets:
            print(pet + ' is ' + pets[pet])
            print('Is that all? (yes/no)')
            confirmAdj = input()
            if confirmAdj == 'yes':
                continue
            elif confirmAdj == 'no':
                print('How would you describe them in a word?')
                newAdj = input()
                pets[pet] = newAdj
                print('Okay. ' + pet + ' is ' + pets[pet] + '.')
    else:
        print('I don\'t know ' + pet + '. Describe them: ')
        newAdj = input()
        pets[pet] = newAdj
        print('Alright. ' + pet + ' is ' + pets[pet] + '.')
