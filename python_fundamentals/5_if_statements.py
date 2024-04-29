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

