#all functions return None if return is not decalred

# define function with parameter


def greet_user(name):
    print(f'Hi there {name}')
    print('Welcome on board')


print("Start")
greet_user("gg")
print("Stop")


# multiple arguments with keyword arguments


def greet_user(first_name, second_name):
    print(f'Hi there {first_name}')
    print('Welcome on board')


print("Start")
greet_user("John", "Smith")
greet_user(second_name="Swanson", first_name="Ron") # keyword arguments are good for code readability
print("Stop")

# in order to be able bypass the arguments, arguments should have default value
