name = input('Ener your name: ')
number = 23
running = True


while running:
    guess = int(input('Enter the number: '))

    if guess == number:
        print(f'Conguratulations {name} you did it!')
        running = False

    elif guess < number:
        print(f'A little higher number please {name}')

    else:
        print(f'Lower number you have to choose {name}')   
else:
    print(f'While loop is over {name}')             
