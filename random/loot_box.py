# Function that returns True 3% of the time and False 97% of the time
# Simulates chance of obtaining bonus from a video game loot chest

from random import random

def get_bonus():
    rand_val = random()

    if rand_val < 0.03:
        return True
    else:
        return False

# Tests the get_bonus function
def test():
    total_true = 0

    for i in range(100):
        current = get_bonus()
        
        if current:
            total_true += 1
    
    print('Out of 100, a bonus was received {} times'.format(total_true))

if __name__ == '__main__': test()