#import adder
import adder , greeter

# to access a function in an imported module 
# use name_of_imported_module, then dot (.) and name_of_functions
#e.g. module.name_of_function
#e.g. adder.add(parameter if any)
value= adder.add(2, 2)
print(value)

#calling another function from adder module (i.e adder.py file)
double_value=adder.double(value)
print(double_value)

#another function from another module,
#greeter module (i.e. greeter.py)
print(greeter.greet("Mike"))


