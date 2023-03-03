# Ok so on day two and class 13 I am getting somewhat lazy because come on... Even though I have not programmed in quite
# a while, I really don't need to re-learn Data Types... Python was the language that I learned how to program at the
# discipline of "Introduction to Computer Science" and then I learned all of the programming paradigms on this language
# later on
import math

# numeric types (integers, floats...)
print("==========================")
print("1. INTEGERS:")
print("==========================")
print("Integers are basically numbers without decimal (PTBR: números inteiros)")
print(1)
print(-23)
print(100)

# On Python, you can convert strings to integers if they are compatible, for instance:
five = int("5")
print("this symbol represents a five: " + str(five) + "\n")

# Operations with Integers:
print("==========================")
print("Operations with Integers:")
print("==========================")
print("Addition (+): 2+1 = " + str(2+1))
print("Subtraction (-): 2-1 = " + str(2-1))
print("Multiplication (*): 2*11 = " + str(2*11))
print("Addition (/): 20/8 = " + str(20/8))
print("The floored quotiente with this simbol -> (//): 20//8 = " + str(20//8))
print('Modulus (%): 2%4 = ' + str(2 % 4))
print("Absolute value (abs(x)): abs(2-4) = " + str(abs(2-4)))
print("A given value in floating point (float(x)): float(2) = " + str(float(2)))
print("A given X on the y-th potency (don't know if this is correctly written in english). "
      "Anyway you write it this way: pow(x,y): pow(2,2) = " + str(pow(2,2)))

# FLOAT (floating point numbers, basically, numbers with decimal points)
# In Python, 5 and 5.0 are different (5 is an int and 5.0 is a float)
type_of_five_int = type(5)
type_of_five_float = type(5.0)
# these two lines were not in the course. In fact, all of this script was not 100% taken from the course, it is just me
# doodling around in the language while teacher talks.
print("\n" + "==========================")
print("2. FLOAT:")
print("==========================")
print("Isn't it funny that data types can be so interesting? For instance, in Python, 5 and 5.0 are different freaking "
      "things, doubt? \n type(5) = " + str(type_of_five_int) + "\n type(5.0) = " + str(type_of_five_float))

# Operations with floats
print("\n" + "==========================")
print("Operations with Floating Pointers:")
print("==========================")

# operations applied to floats:
print("You can round a floating point number with 'round': round(4.3) = " + str(round(4.3)) + "\n" + "round(4.7) = " +
      str(round(4.7)))

# Some methods are in math module and need to be imported
print ("You can also use some methods from the math library (remember to import first): \n" +
       "math.floor(4.8) = " + str(math.floor(4.8)) + "\n" + "math.ceil(4.8) = " + str(math.ceil(4.8)))

# Finished day 2 here. Next up is the class 16 onwards.

# mapping type (dictionaries)

# booleans (True, False)

# and more...