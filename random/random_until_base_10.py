# Prints random integers between 1 and 100 until a value divisible by 10 is hit

from random import randrange

def main():
    print('I generate numbers from 1 to 100 until I pick one divisible by 10.\nHere I go!')

    while True:
        rand_num = randrange(1,101)
        print(rand_num)
        if rand_num % 10 == 0: break

    print('I\'m done!')

main()
        