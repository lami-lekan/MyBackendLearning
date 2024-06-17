#!/usr/bin/python3
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# if alien_0 was shoot down
# shooter will have 5 points
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points.")

# creating key-value pairs
alien_0['x-position'] = 0
alien_0['y-position'] = 25
print(alien_0)

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['x-position'] = 10
alien_1['y-positin'] = 15
print(alien_1)

# modifying values in a dict.
alien_0['color'] = 'red'
alien_1['points'] = 20

print(alien_0, alien_1)

alien_2 = {'color': 'blue', 'x-position': 15, 'y-position': 10, 'speed': 'medium'}
if alien_2['speed'] == 'slow':
    alien_2['x-position'] = alien_2['x-position'] + 1
elif alien_2['speed'] == 'medium':
    alien_2['x-position'] = alien_2['x-position'] + 2
else:
    alien_2['x-position'] = alien_2['x-position'] + 3

print(alien_2['x-position'])

# removing key-val pair
print(alien_2)
print('..deleting *color* key/val now >>>...')
del(alien_2['color'])
print(alien_2)

favourite_language = {
    'sarah': 'java',
    'gibbs': 'python',
    'noah': 'c',
    'tim': 'ruby',
    }

print("Noah's favourite language is " +
    favourite_language['noah'] + ".")

# looping thru a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'erinco',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\n key: " + key)
    print("value: " + value)

for name in favourite_language.keys():
    print(name)

for name in sorted(favourite_language):
    print('\n' + name)
print("\nThese are the list of available programing language: ")
for language in favourite_language.values():
    print(language)

# nesting

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('....')

print(len(aliens))

pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra cheese'],
    }
print('You ordered a ' + pizza['crust'] + '-crust pizza with the following toppings: ')

for topping in pizza['toppings']:
    print(topping)

users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        }
    }

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name)
    print("\tLocation: " + location)
