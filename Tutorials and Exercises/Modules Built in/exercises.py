import random
class dice():

    def roll():
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        results = (x, y)

        return results

print(dice.roll())
