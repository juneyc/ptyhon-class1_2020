import random

num=random.randint(1,21)
print(num)
numGuesses = 0
name=input('hello what is your name? ')
print(name + 'am thinking of a number between 1-21?, can you guess the number?')

while numGuesses<5:
    guess =int(input('Guess a number:'))
    numGuesses +=1
    print(numGuesses)
    guessLeft = 5-numGuesses

    if guess<num:
        guessLeft=str(guessLeft)
        print('your guess is too low! you have '+guessLeft+ 'guesses left')
    else:
        pass
        break
if guess == num:
    num_guesses=str(numGuesses)
    print('good job!!! you guessed correct')
elif guess!=num:
    random_num=str(num)
    print('sorry. the no i was thinking of was '+num+" :)")
