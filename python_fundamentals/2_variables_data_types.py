#!/usr/bin/python3
'''In this chapter of the book, I will learn about different
    kinds of data in python; how to store them in variables
    ; how to use variables in programs.
'''
# using print() function
print("Hello Python World!")

# using variable
message = "Hello Python World!"
print(message)

# updating a variable
message = "Hello Python Crash Course World"
print(message)

# strings
name = "ada lovelace"
print(name.title())

# string methods
name = "Ada Lovelace"
print(name.upper())
print(name.lower())

fav_lang = "python "
print(fav_lang.strip())
 

# string concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

# special characters
sentence = "Programming languages:\n\tPython\n\tC\n\tJava"
print(sentence)

# practice 
name = "Eric"
greet_msg = "Hello " + name + " would you like to learn python"
print(greet_msg)

first_name = "matthew"
last_name = "rimes"
print(name.title() + "\n" + name.upper() + "\n" + name.lower())

print('Albert Einstein once said "A person who never made a mistake never tried new things."')

