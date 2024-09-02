#!/usr/bin/python3
def greet_user(user):
    print("Hello, " + user.title() + "!")

greet_user('mark')

def describe_pet(animal_type, pet_name):
    print("I have a " + animal_type)
    print("My " + animal_type + " name is " + pet_name + ".")


describe_pet("hamster", "harry")
describe_pet(pet_name="willie", animal_type="dog")

def greet_more_user(names):
    for name in names:
        msg = "Hello, " + name + "!"
        print(msg)

usernames = ['Mat', 'Tyler', 'Dan']
greet_more_user(usernames)

