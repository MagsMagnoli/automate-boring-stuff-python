import random

print('Hello. What is your name?')
name = input()

low = 1
high = 20

print('{}, I\'m thinking of a number between {} and {}'.format(name, low, high))
num = random.randint(low, high)

guesses = 7

for guess_num in range(1, guesses):
    print('Take a guess, you have {} remaining'.format(guesses - guess_num + 1))
    guess = int(input())

    if guess < num:
        print('Too low')
    elif guess > num:
        print('Too high')
    else:
        break

if guess == num:
    print('Good job, {}! You guessed my number in {} guesses'.format(name, guess_num))
else:
    print('You\'re out of guesses. The number I was thinking of was {}. You failed. Game over'.format(num))