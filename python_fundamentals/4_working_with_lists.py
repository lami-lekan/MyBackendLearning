#!/usr/bin/python3
# using 'for' loop on lists
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you everyone that was a great magic show.")

print()
pizzas = ['New york style', 'Roman', 'Chicago style']
for pizza in pizzas:
    print(pizza + ' pizza' + ' is one of the best.')
print("I really love pizza.")

# making numerical list
print()
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

print()

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print(sum(squares))
