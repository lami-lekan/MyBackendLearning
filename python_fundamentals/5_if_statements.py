#!/usr/bin/python3
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
car = 'bmw'
print(car == 'bmw')

car = 'Audi'
print(car.lower() == 'audi')
print(car)

requested_toppings = 'mushrooms'

if requested_toppings != 'anchovies':
    print('Hold the anchovies')

age_0 = 20
age_1 = 24

print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

items = ['ball', 'can', 'broom']
print('broom' in items)
print('bin' in items)
print('can' not in items)

age = 17
if age >= 18:
    print("You are eligible to vote.")
    print("Have you registered to vote yet?")
else:
    print("You are not eligible to vote.")
    print("Please register when you are 18 or above.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10
print("Your admission cost is $" + str(price) + ".")

requested_toppings = ["mushroom", "extra cheese", "green pepper"]

if "mushroom" in requested_toppings:
    print("Adding mushroom...")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese...")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni...")
print("Pizza finished")

alien_color = ['yellow', 'green', 'red']
alien_shot = 'yellow'

if alien_shot == 'green':
    print("5 points earned")
else:
    print("0 point")

for toppings in requested_toppings:
    if toppings == "green pepper":
        print("Sorry we are out of green pepper")
    else:
        print("Adding " + toppings + ".")
print("Pizza ready.")

available_toppings = ["extra cheese", "green pepper"]

for toppings in requested_toppings:
    if toppings in available_toppings:
        print("Adding " + toppings + ".")
    else:
        print("Sorry, we do not have " + toppings + " right now.")
print("Pizza ready!")

username = ["eric", "admin", "jared", "tim"]
new_usr = ["eric", "tim", "white", "paige"]

for usr in username:
    if usr == "admin":
        print("Hello " + usr.title() + " would you like to see a status report?" )
    else:
        print("Hello " + usr.title() + " thank you for logging in again.")

for usr in new_usr:
    if usr in username:
        print(usr +  " already in use, please pick another.")
    else:
        print("Welcome " + usr.title() + ".")
