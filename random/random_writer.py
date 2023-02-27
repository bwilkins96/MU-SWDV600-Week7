# Writes a file with 30 lines of 2 random float values
# e.g. 12.0-13.0, 15.0-20.0

from random import random

def main():
    out_file = open('random-floats.txt', 'w')

    for i in range(30):
        val_1 = 12 + random()
        val_2 = 15 + (random() * 5)

        print('{}, {}'.format(val_1, val_2), file=out_file)

    out_file.close()
    print('Done writing to random-floats.txt')

main()