#sectet nuber exercise

secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input(f'{guess_count + 1} Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won')
        break
# so this else is tricky. if this else is after if then it will be printed after every guess, but when after while it will be once when while completed
else:
    print('you guessed wrong')