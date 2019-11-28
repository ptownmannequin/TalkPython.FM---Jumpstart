import random

print('--------------------------------------------')
print('            GUESS THAT NUMBER!!!!')
print('--------------------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('Enter Player Name: ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess > the_number:
        print('{1}, your guess of {0} is HIGHER than the number. Please try again: '.format(guess, name))
    elif guess < the_number:
        print('{1}, your guess of {0} is LOWER than the number. Please try again: '.format(guess, name))
    else:
        print('Congratulations! You guessed the correct number!!! ')
