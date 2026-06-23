# MATCH-CASE Statements
# Like if-else from java and c, python has match-case but
# Very important thing is that here the syntax doesn't call for break; statement
# Syntax:
# match variable_name:
#     case (pattern1):
#         statement 1
#     case (pattern2):
#         statement 2
#     .
#     .
#     .
#     case (pattern n):
#         statement n

test_num = int(input("Enter a number inbetween 1 to 10: "))
match test_num:
    case 0:
        print("The number is 0.")
    case 4 if test_num % 2 == 0:
        print("The number is 4")
    case _ if test_num >= 5:
        # we can insert if conditions too for more elaborate conditions
        print("The number is greater than 5")
    case _:
        # This _ is a default case just like the else statement from if-else and will only execute
        # when every other case is failed
        print("The number is ", test_num)


# Break&Continue
# Break -> It stops a part of the code or the very loop it lies within.
# essentially saying that LOOP KO CHODKAR CHALE JAO.
test = 'Tushar'
for i in test:
    print(i)
    if i == 'h':
        break
    else:
        print('is SEXY')

# Continue -> It skips the code following the continue statement and starts the next iteration.
# essentially saying that ITERATION KO CHODKAR KAR NIKAL JAO.
for i in test:
    print(i)
    if i == "h":
        continue
    else:
        print('is sexy')
