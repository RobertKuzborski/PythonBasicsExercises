# find highest number

numbers = [1, 2, 3, 4, 5, 6, 9, 7, 8]
highest_number = 0
for number in numbers:
    #print(number)
    if highest_number < number:
        highest_number = number
print(highest_number)

# program to remove duplicates
print(' Program to remove duplicates \n')

numbers = [1, 5, 2, 1, 9, 9, 9, 9, 7, 4, 5, 5, 5, 6, 9,]

original_numbers = numbers.copy()
index = 0

for number in numbers:
    duplicates = numbers.count(number)
    print(f'i {index} : for number {number} there are {duplicates} entries')
    index += 1
    if duplicates > 1:
        print(f'There is {duplicates-1} duplicate of number {number}')
        while duplicates > 1:
            numbers.remove(number)
            duplicates -= 1
            print(f'duplicate of {number} has been removed and there are {duplicates -1} duplicates left')


print(f'{original_numbers} \t < original numbers')
print(f'{numbers} \t < no duplicate numbers')

# program to remove numbers : the sollution way shorter then mine
numbers = [1, 5, 2, 1, 9, 9, 9, 9, 7, 4, 5, 5, 5, 6, 9,]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(numbers)
print(uniques)