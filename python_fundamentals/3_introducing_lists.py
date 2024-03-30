#!/usr/bin/python3

# Creating a list of bicycles brand
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# Accessing elements in a list using their index
# list index is always off by 1 to it elem position 
print(bicycles[0])
print(bicycles[2].title())

# -1 index is the last elem in the list
print(bicycles[-1])

# changing, adding, and removing elements
motorcycles = ['baja', 'honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[1] = 'ducati'
print(motorcycles)
motorcycles.append('baja')
print(motorcycles)
print()
phones = []
phones.append('iphone')
print(phones)
phones.append('samsung')
print(phones)
phones.insert(1, 'itel')
print(phones)
phones.insert(-2, 'nokia')
print(phones)

del motorcycles[1]
print(motorcycles)
popped_phone = phones.pop(1)
print(phones)
print(popped_phone)
del_baja = motorcycles.remove('baja')
print(motorcycles)

guest_list = ['Papa', 'Mama', 'Sisters', 'Brother']
print('Invitation: Dinner party for; ' + guest_list[0] + ',' + guest_list[1] + ',' + guest_list[2] + ',' + guest_list[3] + '.')

# organizing a list
cars = ['bugatti', 'bmw', 'audi', 'toyota', 'hyundai', 'ferrari']
cars.sort(reverse=True)
print(cars)
print(sorted(cars))
print(cars)

apps = ['facebook', 'twitter', 'instagram', 'whatsapp']
print(apps)
apps.reverse()
print(apps)

print(len(apps))
