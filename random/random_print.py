# Prints out a statement based on a random value
# 35% chance of printing statements 1 or 3, 30% chance of statement 2

from random import random

def main():
    rand_val = random()

    if rand_val < 0.35:
        print('This is as likely as the last possible statement')
    elif rand_val < 0.65:
        print('This is slightly less likely than the other 2 statements')
    else:
        print('This is as likely as the first possible statement')

main()