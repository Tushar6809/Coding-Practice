# Python was introduced by Van Rossum in 1989.
# It is a High-Level language. Also it is platform independent.
# It follows OOP that is object oriented programming.
print("Hello World")
# we don't need to declare the variables with data types in python.
# Like Java, so thats why it is considered as dynamically typed language.
a = 10
b = 204
# Python has two types of modules:
# 1. Built-in Modules: These Modules already come with python. There is no need to pip install them.
# 2. External modules: These Modules are needed to be downloaded using pip install command.
print("a + b =", a+b)
# what is pip?
# Its a package manager for python. Its full form is "Pip install packages".
# This is used to downlaod and manage external modules in python.

# In java and c, we need to import the scanner to take input from the user but in python
# we can take the input directly using the below mentioned Function.
# We can also specify the data type like a = int(input("Enter a number:")) to take interger as input and so on.
# By default the input takes string as input.
a = input("Enter Your Name:")
# so if we take integer input as a string then we cannot perform maths fuctions on it.
print("Your name is ", a)
print("Your name is", (a))
# Repl-> Read-Evaluate-Print-loop.
# It is an interactive programming environment that takes single user inputs, evaluates them
# and returns the result to the user.
# It is a simple way to test code snippets and debug code.

# for an any function to work in python. we need to use parenthesis. like print() and input() functions.
# Quick controls:
# ctrl + enter/R -> To run the code.
# ctrl + backslash + enter -> To run the code in debug mode.
# ctrl + forwardslash -> to turn code into comments and vice versa. Like i did here.
# Alt + select -> to select multiple words and edit them at the same time.
# Alt + shift + down arrow -> to copy the line and paste it as multiple lines. Like i did here.
pi = 3.14
pi = 3.14
pi = 3.14
pi = 3.14
pi = 3.14

# Some Escape sequence characters i learned in python as of now are:
# \t -> for space
# \n -> for new line
# \" -> for double quotes". It is used to print double quotes in output. as python cant understand
# the multiple double quotes in a string. so we use \" to print double quotes in output.
# and i dont know what this is but here it is
# if we write "hi"*2 then it will print hihi.
print("hello \"world")
print("Hello\tWorld")
print("Hello \n World")
print("Hello world"*4)

# In python, all things are objects.
# Like Java and C, we have arrays in python called lists.
# They are:
# dict -> dictionary, these are mutable and unordered collection of key-value pairs. They are defined using curly braces {}.
# tuple -> these are immutable and ordered collection of items. They are defined using parentheses ().
# list -> these are mutable and ordered collection of items. They are defined using square brackets [].

# Operators in python are:
# Arithmetic operators: +, -, *, /, //, %, **. I just know these now.
# + -> addition
# - -> subtraction
# * -> multiplication
# / -> division
# we already the above and now lets dicuss the remaining three


# First the famous formula: Dividend = Divisor * Quotient + Remainder
# for example, 100 = 3 * 33 + 1
# // -> floor division -> It returns the quotient from above example.
# % -> modulus -> It returns the remainder from above example.
print("100//3 =", 100//3)
print("100%3 =", 100 % 3)

# ** -> exponentiation -> This here returns the result of any power to the base number.
# For example, 2**3 will return 8.
print("2**3 =", 2**3)

# What is Type Casting?
# In simple terms, it is the conversion of  one data type to another data type.
# For Example,
c = input("Enter a number:")
print(" the number is ", int(c))
print("The data type of c is", type(c))
# In the above code, we took input as a string and
# then we converted it to an integer using int() function.

# some data types are int, float, str, bool, list, tuple, dict, set and so on.
# There are two types of type casting:
# 1. Implicit: This conversion is done by the python interpreter automatically.
# For example, if we add an integer and a float, the result will be a float.

# 2. Explicit: This conversion is done by the programmer using built-in functions like int(), float(), str() and so on.
# Like the example above where we used int() function to convert the string input to an integer.

# But how do we know which data type will be converted and which will not be converted in implicit?
# Its by knowing the precision of the data types
# like the float data type has decimal points while int has none.
# so when we add both dta types, the result is float output.
