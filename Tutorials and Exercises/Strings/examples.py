birth_year: int = input('Birth Year: ')
print(type(birth_year))
age: int = 2019 - int(birth_year)
print(type(age))
print(age)
#
weight = int(input('Weight in kg '))
print(type(weight))
print(weight)

# trim strings by indexes
name = 'Jennifer'
print(name[1:-1])

# insert string variables into string
first = 'John'
last = 'Smith'
msg = f' {first} [{last}] is a coder'
print(msg)

# string operations like length, upper and lower cases
course = 'Python for beginners'
print(len(course))
print(course.upper())
print(course.find('n'))
print(course)