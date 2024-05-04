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

