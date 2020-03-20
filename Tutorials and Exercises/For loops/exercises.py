# calculate prices , so price is current value from array of prices
prices = [10, 20, 70]
total = 0
for price in prices:
    total += price
print(f'total {total}')

print("\n")

for x in range (4):
    for y in range(3):
        print(f'({x}), ({y})')

# print F from asterix
numbers = [5, 2, 5, 2, 2]

for x in numbers:
    print('*' * x)

# print F in dificult way

numbers = [5, 2, 5, 2, 2]

for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)
