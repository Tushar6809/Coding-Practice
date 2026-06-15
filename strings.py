Boy_one = "John"
Boy_two = 'Jack'
# we can either use + or, to concatenate strings.
print("hello" + Boy_one, Boy_two)

# We can use the triple single or double qoutes to store multi line strings in pytghon.
Multiple_lines = '''augwgwuidgi
jbbvhrvrrjb
 rn3brkrbi3rgubr
 nw ak rbrbb'''

# here we used both single and double quotes to store a string with quotes in it.
Sent = 'Tushar said,"You are a bitch"'
print(Sent)
# so what will happen if we use the same quotes to store a string with quotes in it.
# tke = "Tushar said,"You are a bitch""
# print(tke)
# see it caused error because we used the same quotes to store a string with quotes in it.

# when we want to print only one or a specific character from a string we can use indexing.
# indexing starts from 0 and goes on till the length of the string - 1.
print(Sent[0])
print(Sent[7])
# if we want to print the whole string like this without using the print function againa and again.
# We can use for loop
# For example: we will three syntax here
length = len(Sent)
print(length)
for i in range(length):
    print(Sent[i])
#      OR
for character in Sent:
    print(character)
#      OR
for i in Sent:
    print(i)

# WE WILL SEE  SLICING NOW.
# String is like a array of characters and remember string is not an array
# rather it is a sequence of characters.
# slicing is used to get a specific part of the string
# For eample:
pie = "Applepie"  # Syntax:  variable[start index:end index]
print(pie[0:5])           # start index from where it starts
print(pie[:5])            # till end (index-1)
print(pie[:])
print(pie[0:])
print(pie[1:])
print(pie[5])
print(pie[2:6])
print(pie[0:-3])          # -3-> [len(pie)-3]
print(pie[:-3])
print(pie[0:len(pie)-3])
print(pie[1:-6])
print(pie[-2:-4])        # -2 = 8-2=6 & -4 = 8-4=4. so [6:4] doesnt make sense.
