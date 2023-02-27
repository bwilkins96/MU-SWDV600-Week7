# Prints 10 random even ratings between 30 and 100

from random import randrange

def main():
    print('This program produces 10 random even ratings between 30 and 100')

    for i in range(10):
        rating = randrange(30, 101, 2)
        print(rating)

main()