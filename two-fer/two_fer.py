import sys

name = raw_input("What is your name?")

def two_fer(name):
    if name:
        print("One for " + name + ", one for me.")
    else:
        print("One for you, one for me.")

two_fer(name)
