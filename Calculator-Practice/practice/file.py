# single line commemt variabe declarations
# variable declared using a number that's an integer
num1 = 42
# variable declared using a float
num2 = 2.3
# variable declared with a boolean
boolean = True
# variable declared with a string
string = 'Hello World'
# variable declared with a list of strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declared with a dictionary of strings, numbers, and a boolean
person = {'name': 'John', 'location': 'Salt Lake',
          'age': 37, 'is_balding': False}
# variable declared with strings
fruit = ('blueberry', 'strawberry', 'banana')
# log statement checking a variables type
print(type(fruit))
# a log statement asking for index 1 from the list assigned to the variable of pizza_toppings
print(pizza_toppings[1])
# a variable containing a list having a function used to add a string to the end of the list
pizza_toppings.append('Mushrooms')
# a log statement logging a value in a dictionary assigned to a variable
print(person['name'])
# a variable who's value inside a dictionary assigned to a variable is being changed to another string
person['name'] = 'George'
#  a variable containing a dictionary having it's values changed
person['eye_color'] = 'blue'
# log function printing an index value of a list inside a variable
print(fruit[2])
# if statement with a condition
if num1 > 45:
    print("It's greater")
    # else statement
else:
    print("It's lower")
# length check = len()
if len(string) < 5:
    print("It's a short word!")
    # else if statement checking the length of a string
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# for loop checking a range
for x in range(5):
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0
# a while loop with a start and stop condition toexecute a log
while (x < 5):
    print(x)
    x += 1
# calling a variable and removing end value
pizza_toppings.pop()
# calling a variable and removing the first index from its list
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break


def print_hello_ten_times():
    for num in range(10):
        print('Hello')


print_hello_ten_times()


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4)


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
