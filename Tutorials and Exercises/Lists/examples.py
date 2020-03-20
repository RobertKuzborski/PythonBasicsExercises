# created list
names = ['John', 'Bob', 'Marry', 'Tom', 'Peter']
print(names) # print whole list
print(names[0]) # print index, or first entry
print(names[-1]) # print last entry
print(names[2:]) # print range of entries starting at to the end
print(names[:2]) # print range of entries until index2
print(names[2:4]) # print range of entries from : to

# and important thing is that when using brackets it returns new list not original
# so its not modifying the list itself just tales entries

# 2D lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix[0][1] = 20
print(matrix[0][1])

for row in matrix:
    for item in row:
        print(item)

print(matrix)

# list operations

numbers = [1, 5, 2, 1, 7, 4, 5]
numbers.append(20) # add number to the end of the list
print(numbers)
numbers.insert(0, 50) # insert the number at the position
print(numbers)
numbers.remove(1) # remove number from the list !!!
# removes the first number equal to the requested number, NOT THE INDEX!!
print(numbers)
numbers.pop() # remove last item in the list
print(numbers)
numbers.pop(0) # remove entry at the index
print(numbers)
print(numbers.index(7)) # print the index of requested number
# if number is not in the list it throws exception

print(50 in numbers) # to check if the number is in the list: Boolean return
print(7 in numbers)

print(numbers.count(5)) # counts how many fives are in the list

print(numbers)
numbers.sort() # sorts the numbers
print(numbers)
numbers.reverse() # reverses the list
print(numbers)

numbers2 = numbers.copy() # copies the numbers into new variable
numbers3 = numbers # this does not create duplicate, but assigns pointer to original variable in this case numbers
numbers.append(100)

print(f'n3 {numbers3}')
print(f'n2 {numbers2}')
print(f'n0 {numbers}')

numbers.clear() # clear the whole list
print(numbers)

# unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates
print(x, y, z)
#it is exatly the same as below just less lines of code
# x = coordinates[0]
# y = coordinates[1]
# z = coordinates[2]
