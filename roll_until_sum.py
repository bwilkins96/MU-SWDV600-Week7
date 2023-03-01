# Simulates rolling two 6-sided dice until their sum is an inputted value

from random import randrange

class Dice:
    'A dice class designed for Maryville University'

    def __init__(self, num_dice):
        """
        Initializes list with n number of die values
        e.g. Dice(2) produces an instance with 2 die values
        """
        self.dice = [1] * num_dice
        self.roll()

    def get_dice(self):
        'Returns a copy of the dice list'
        return self.dice[:]

    def roll(self):
        'Changes the values in the dice list to random values between 1 and 6'
        for i in range(len(self.dice)):
            self.dice[i] = randrange(1, 7)

    def sum_dice(self):
        'Returns the sum of all values in the dice list'
        sum = 0
        for die in self.get_dice():
            sum += die
        
        return sum

# Gets and validates target sum input
def get_target_sum():
    while True:
        try:
            target_sum = int(input('Enter the target sum to roll for: '))
        except:
            target_sum = 0

        if target_sum >= 2 and target_sum <= 12: break
        print('Enter a value between 2 and 12!')

    return target_sum

# Prints result of rolling 2 die
def print_results(dice):
    die_1, die_2 = dice.get_dice()
    print(f'Roll: {die_1} and {die_2}, sum is {dice.sum_dice()}')

def main():
    print('This program rolls two 6-sided dice until their sum is a given target value.')
    target_sum = get_target_sum()

    # Initializes to 2 die and primes for while loop
    dice = Dice(2)
    rolls = 1
    print()
    print_results(dice)

    # Rolls dice and prints results until target sum is reached
    while dice.sum_dice() != target_sum:
        dice.roll()
        rolls += 1
        print_results(dice)

    if rolls == 1:
        print('\nGot it in only 1 roll!')
    else:  
        print(f'\nGot it in {rolls} rolls!')

main()


    