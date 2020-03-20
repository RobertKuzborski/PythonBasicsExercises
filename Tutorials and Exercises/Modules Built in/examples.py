#roll dice
import random


class Dice:
    def roll(self):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        results = (x, y)
        return x, y   # function returns tupple


dice = Dice()
print(dice.roll())