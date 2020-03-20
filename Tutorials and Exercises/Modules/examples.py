#Modules

#create new.py file in the same folder and then import new
#anoter file is imported and it is possible to access its functions by using new.ClassName()

import modulexample

print(modulexample.print_some_function(70))
modulexample.greet_user("Soren","Kebab")


#as well it is possible to import only some of the functions from another file

from moduleexample2 import greet_user

# greet_user("Raven","Kebab")		#and in this case the class is imported directly, so its unnecessary to refer to converters.
print(greet_user("Raven","Kebab")) # because it has return value it prints it

import somemodule as sm # shortens the name of module