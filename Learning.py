
print("Hello Python")

# VARIABLES

message = "Hello python world!"
print(message)

a = 12
print(a)

a = 11
print(a)

b = 25
print(b)

temp = 11
a = 25
b = temp
print(b)
print(a)
# strings
print("The language 'Python' is named after Monty Python, not the snake.")

# methods - used to perform a manipulation to a piece of data
name = "ievey kay"
print(name.title())

name = "Ievey kay"
print(name.upper())
print(name.lower())

# Concatenating
F_Name = "ievey"
L_Name = "hidden"
Full_Name = F_Name + " " + L_Name
print(Full_Name)

print("Hello," + Full_Name.title() + "!")

text = "Hello," + Full_Name.title() + "!"
print(text)

# \t - horizontal tab \n- new line
print("\tPython")
print("\nKali\nLinux")
print("\n\tKali\n\tLinux")

# Stripping whitespace lstrip-left, rstrip-right, strip-both sides
# For the output to be stored when changed use a variable
new_language = " python"
new_language = new_language.lstrip()
print(new_language)

new_language = "python "
new_language = new_language.rstrip()
print(new_language)

new_language = " python "
new_language = new_language.strip()
print(new_language)

# Exercise
name = "Gladwell Malcolm"
personal_message = name.title() + " ""I love your novels"
print(name)
print(personal_message)

# doubleqoutes - escape with backslash or single quotes
print("Barrack Obama\"Yes We Can\"")
print('"Yes We Can"')

# NUMBERS
answer = (3 ** 2)
print(answer)

# converting integers to strings-when python interpreter interprets the numbers as a string,use str()
age = 23
birthday_wishes = "Happy" + " " + str(age) + "rd birthday!"
print(birthday_wishes)

# Zen Philosophy
import this

# LIST[] - Collection of items in a particular order, Is Accessed by using index
fruits = ['apple', 'mango', 'orange', 'peach', 'kiwi']
print(fruits[0])
print(fruits[2])

fruits = ['apple', 'mango', 'orange', 'peach', 'kiwi']
print(fruits[0].title())

# if list is long you can access the last item from the list (-1 , -2 ...
fruits = ['apple', 'mango', 'orange', 'peach', 'kiwi']
print(fruits[-1])
print(fruits[-2])

vegeterian = "Today I ate" + " " + fruits[-1].title() + "."
print(vegeterian)

# Changing, Adding, Removing elements
# modifying elements in a list
Guest_list = ['Oprah', 'Mitchell', 'Kelsy', 'John']
print(Guest_list)
Guest_list[0] = 'HailMary'
print(Guest_list)

# Adding elements to a list
# append - new item is added to the end of the list
Guest_list.append('Peter')
print(Guest_list)
# Defining an empty list using append - want users to define own list
Guest_list = []
Guest_list.append('HailMary')
Guest_list.append('Mitchell')
Guest_list.append('Kelsy')
Guest_list.append('John')
Guest_list.append('Peter')
print(Guest_list)

# inserting elements to a list - operation shifts every other value
Guest_list.insert(0, 'Jakes')
print(Guest_list)

# Removing elements from a list.
# using - del (if you know index)(You can no longer access them)
del Guest_list[-1]
print(Guest_list)
del Guest_list[4]
print(Guest_list)

# using - pop (You can access them later)-last from end list
Guest_list = ['mitchell','kelsy','hailMary','jakes']
print(Guest_list)
popped_Guest = Guest_list.pop()
print(Guest_list)
print("Sorry" + " "+popped_Guest.title() + " "+"the party has been cancelled.")
# popping from any positon
another_Guest = Guest_list.pop(0)
print("Sorry" + " "+another_Guest.title() + " "+"the party has been cancelled.")

# Removing an item by value - if you know the Item
Guest_list.remove('kelsy')
print(Guest_list)

extended_invite = 'hailMary'
Guest_list.remove(extended_invite)
print("\n" + extended_invite.title() + " " + "you have an extended invite")

# Organizing a list
# Using - sort (permanently)(alphabetically)
Guest_list = ['Peterson', 'Johnson', 'Anthony', 'Eilish']
Guest_list.sort()
print(Guest_list)
# reverse - argument(alphabetically)
Guest_list.sort(reverse=True)
print(Guest_list)

# sort - temporarily
Guest_list = ['Peterson', 'Johnson', 'Anthony', 'Eilish']
print(sorted(Guest_list))
# Guest_list = ['Peterson', 'Johnson', 'Anthony', 'Eilish']
print(Guest_list)

# print in reverse order
Guest_list = ['Peterson', 'Johnson', 'Anthony', 'Eilish']
Guest_list.reverse()
print(Guest_list)

# length of a list
Guest_list = ['Peterson', 'Johnson', 'Anthony', 'Eilish']
No_of_guests = len(Guest_list)
print(No_of_guests)

# LOOP A LIST
# for loop - set of steps is repeated once for each item in the list.

# cake - variable(rep a single item to make it meaningful)
# indent print() - it's inside the for loop(4spaces)
Cakes = ['carrot', 'velvet', 'forest', 'fudge']
for cake in Cakes:
    print(cake)

Cakes = ['carrot', 'velvet', 'forest', 'fudge']
for cake in Cakes:
    print("I love"+" "+cake.title() + "cake.")
    print("I will bake" + " " + cake.title() + "cake.\n")
print("All my cakes are sweet!!")

# numerical list
# python's range

for value in range(1, 6):
    print(value)

# to print the range of numbers in a list - list()
numbers = list(range(1, 6))
print(numbers)

# list even numbers between 1-10
# start at 2, end at 10 to each value add 2
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# cube
cubed_numbers = []
for cubed in range(1, 11):
    cubed_numbers.append(cubed**3)
print(cubed_numbers)

cubed_numbers = []
for value in range(1, 11):
    cubed = value**3
    cubed_numbers.append(cubed)
print(cubed_numbers)

cubed_numbers = [value**3 for value in range(1, 11)]
print(cubed_numbers)

# max,min,sum
digits = list(range(0, 10))
min_value = min(digits)
print(min_value)

digits = list(range(0, 10))
max_value = max(digits)
print(max_value)

digits = list(range(0, 10))
sum_value = sum(digits)
print(sum_value)

# slice - process your data in chunks of specific sizes
# start:end
Guest_list = ['Peterson', 'Johnson', 'Anthony', 'Eilish']
print(Guest_list[0:3])
print(Guest_list[:3])
print(Guest_list[1:])
print(Guest_list[:-2])

Guest_list = ['Peterson', 'Johnson', 'Anthony', 'Eilish']
print("Short-listed guest list:")
guests = Guest_list[:2]
print(guests)

print("Short-listed guest list:")
for guests in Guest_list[:2]:
    print(guests)

# Copy - use slice
my_cakes = ['carrot', 'velvet', 'forest', 'fudge']
friend_cakes = my_cakes[:]
my_cakes.append('chiffon')
friend_cakes.append('chocolate')
print("My cakes are:")
print(my_cakes)
print("\nMy friend's cakes are:")
print(friend_cakes)

my_cream = ['vanilla', 'chocolate', 'strawberry']
friend_cream = my_cream[:]
new_cream = 'cheese'
new_cream2 = 'blueberry'

my_cream.append(new_cream)
print("My new cream are:")
for new_cream in my_cream:
    print(new_cream)

friend_cream.append(new_cream2)
print("\nMy friend's new cream are:")
for new_cream2 in friend_cream:
    print(new_cream2)

# Tuple - set of values that do not change
library_books = ('blink', 'Outliers', 'Mamba', 'Martin Luther')
print(library_books[1])
print(library_books[0])

# library_books[0] = 'Bitter Sweet'

print("Original books:")
for books in library_books:
    print(books)

library_books = ('Carry me across', 'Fortune', 'Legacy', 'Kobe')
print("\nNew books:")
for books in library_books:
    print(books)

# IF STATEMENTS
cars = ['audi', 'bmw', 'mercedes', 'discovery']
for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())

# checking for equality
color = 'Red'
if color == 'Red':
    print(color.upper())
else:
    print(color.title())

color = 'Red'
if color == 'orange':
    print(color.upper())
else:
    print(color.title())

# checking for inequality
new_destination = 'Baltimore'
if new_destination != 'Malibu':
    print("change of plans,welcome to Malibu")

# numerical comparisons
# and - fails when either one test fails or both tests fails
age_0 = 37
age_1 = 35
if age_0 >= 30 and age_1 >= 30:
    # if age_0 >= 40 and age_1 >= 40:
    print("True")

# or - fails only when both individual tests fail
age_0 = 37
age_1 = 35
if age_0 >= 36 or age_1 >= 36:
    print("True")

age_0 = 37
age_1 = 35
if age_0 >= 40 or age_1 >= 40:
    print("both tests fail hence no output")

# Find value in a list - use in
new_destination = ['baltimore', 'malibu', 'philadelphia']
if 'baltimore' in new_destination:
    # if 'chicago' in new_destination:
    print("in the list")

new_destinations = ['baltimore', 'malibu', 'philadelphia']
for destination in new_destinations:
    print("Arriving" + " "+destination + ".")
print("\nDestination reached!")

available_destinations = ['mexico', 'cuba', 'baltimore', 'malibu', 'philadelphia']
requested_destinations = ['malibu', 'greece', 'baltimore']
for requested_destination in requested_destinations:
    if requested_destination in available_destinations:
        print("Booking" + " " + requested_destination + ".")
    else:
        print("Sorry," + requested_destination + " " + "not in the list")

# Check if value is not in a list - use not
visited_pages = ['google', 'github', 'medium']
page = 'Tryhackme'
if page not in visited_pages:
    print(page.upper() + ",is not in the list.")

# simple if statements
age = 19
if age >= 18:
    print("Do you have a national ID?")
    print("You can take liquor")

# if-else block
age = 17
if age >= 18:
    print("Do you have a national ID?")
    print("You can take liquor")
else:
    print("Sorry you need to have a national ID")
    print("When you turn 18 you can take liquor")

# elseif ladder

# 50 is the passmark to proceed to the next class
# a student's entry score is 80
marks = 80
if marks <= 49:
    print("Below average")
elif marks == 50:
    print("average")
else:
    print("above average")

# DICTIONARIES {} allows you to connect pieces of unrelated information.
# Is a collection of key value pairs - each key is connected to a value

f1_players = {'type': 'ferrari', 'sponsor': 'redbull'}
print(f1_players['type'])
print(f1_players['sponsor'])

# add new key-value pairs
f1_players = {'type': 'ferrari', 'sponsor': 'redbull'}
f1_players['score'] = 87
f1_players['country'] = 'AUS'
print(f1_players)
new_score = f1_players['score']
print("Hamilton" + " " + str(new_score)+" " + "points!")

# starting with an empty dictionary
# f1_players = {}

# Modifying values in a Dictionary
f1_players = {'type': 'ferrari'}
f1_players['type'] = 'mercedes'
print(f1_players)

f1_players = {'pole_position': 103, 'speed': 'medium'}
print("Original pole-position:" + str(f1_players['pole_position']))
if f1_players['speed'] == 'slow':
    pole_increment = 1
elif f1_players['speed'] == 'medium':
    pole_increment = 2
else:
    pole_increment = 3
# The new pole position is the old position plus the increment
f1_players['pole_position'] = f1_players['pole_position'] + pole_increment
print("New pole-position:" + str(f1_players['pole_position']))

# Removing key values - del removes permanently
f1_players = {'type': 'ferrari', 'sponsor': 'redbull'}
del f1_players['sponsor']
print(f1_players)

# A dictionary of similar objects
favorite_numbers = {
    'Anna': 7,
    'Ken': 5,
    'Peter': 9,
    'Kelly': 11,
    }
print("Ken's favorite number is:" + str(favorite_numbers['Ken']))

# Looping through a Dictionary









