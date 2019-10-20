from random import randint
from sys import argv

first_arg = int(argv[1])
sec_arg = int(argv[2])
solution = randint(first_arg, sec_arg)

while True:
    guess = int(input(f'Guess the number between {first_arg} and {sec_arg}\n'))
    if guess == solution:
        print("You are right!")
        break
