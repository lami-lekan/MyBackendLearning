#!/usr/bin/python3
message = input("Tell me something and I will repeat it back to you: ")
print(message)
prompt = "If you tell us who you are we can personalize the messages you see."
prompt += "\nWhat is your name? "
name = input(prompt)
print("\nHello, " + name + "!")

prompt = "\nPlease enter the name of a city you have visited:"
prompt +="\n(Enter 'quit' when done.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to" + city.title() + "!")

current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

pets = ['cat', 'dog', 'cat', 'snake', 'spider', 'monkey', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)
