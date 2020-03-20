# dictionaries -  sth as struct

customer = {
    "name": "John Smith",
    "age" : 30,
    "is_verified" : True
}
print(customer["name"])
# print(customer["Name"]) # if there is no entry the exception occurs
# print(customer["sth"]) # same as above

print(customer.get("sth")) # so if we use get, program wont crash
print(customer.get("sth", "default value")) # or we can set default

customer["name"] = 'Jack Smith' # that is how to modify individual items
print(customer["name"])
customer["sth"] = "something" # or we can add the new entry into dictionary like that
print(customer["sth"])