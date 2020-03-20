# name = input('Enter the name: ')
#
# if len(name) < 3:
#     print('name cant be less than 3 characters')
# elif len(name) > 30:
#     print('name cant be more than 30 characters')
# else:
#     print(f'entered name is valid and it is {name}, welcome ')


### Try repetative code until condition met in this case age validity
while True:
    try:
        age = int(input("Please enter your age: "))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue

    if age < 0:
        print("Sorry, your response must not be negative.")
        continue
    elif age > 100:
        print("you r too old")
        continue
    else:
        #age was successfully parsed, and we're happy with its value.
        #we're ready to exit the loop.
        break
if age >= 18:
    print("You are able to vote in the United States!")
else:
    print("You are not able to vote in the United States.")