# Simulates rolling two 6-sided dice until their sum is an inputted value

from random import randrange

class Dice:
    def __init__(self, num_dice):
        self.dice = [1] * num_dice
        self.roll()

    def get_dice(self):
        return self.dice[:]

    def roll(self):
        for i in range(len(self.dice)):
            self.dice[i] = randrange(1, 7)

    def sum_dice(self):
        sum = 0
        for die in self.get_dice():
            sum += die
        
        return sum

def get_target_sum():
    while True:
        try:
            target_sum = int(input('Enter the target sum to roll for: '))
        except:
            target_sum = 0

        if target_sum >= 2 and target_sum <= 12: break
        print('Enter a value between 2 and 12!')

    return target_sum

def print_results(dice):
    die_1, die_2 = dice.get_dice()
    print(f'Roll: {die_1} and {die_2}, sum is {dice.sum_dice()}')

def main():
    print('This program rolls two 6-sided dice until their sum is a given target value.')
    target_sum = get_target_sum()

    dice = Dice(2)
    rolls = 1
    print()
    print_results(dice)

    while dice.sum_dice() != target_sum:
        dice.roll()
        rolls += 1
        print_results(dice)

    if rolls == 1:
        print('\nGot it in only 1 roll!')
    else:  
        print(f'\nGot it in {rolls} rolls!')

main()


    