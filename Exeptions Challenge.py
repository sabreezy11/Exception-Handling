##CHALLENGE VIDEO 290##
# 1. Ask the used to type in two integer numbers, then print out their first number divided by their second.
# 2. The program shouldn't crash, no matter what the user types in
# 3. Hint: If you have to do the same thing more than once, that sounds like a good use for a function

import sys # used to give exit codes upon code termination

def getint(prompt):
    """Function will keep asking for a value until valid value is entered"""
    while True: #will keep looping till valid number is entered
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)
        finally:
            print("The finally clause always executes!") #executes regardless if
            # an execution was handled or not.

first = getint("Please enter first number: ")
second = getint("Please enter second number: ")

try:
    print("{} divided by {} is {}".format(first, second, first/second))
except ZeroDivisionError:
    print("What are you doing dividing by zero?")
    sys.exit(2)
else:
    print("Division performed successfully")  # only executed if the 'try' completes





##NOTES##
# 1. 'finally' clause starts with the keyword 'finally', followed by the block of code that you want to execute,
# whether an exception was raised or not.
# 2. If you use a 'finally' clause, it must come after all your 'except' clauses.
# 3. An 'else' clause is executed if the code in the 'try' block doesn't raise an exception.
# this is equivalent to the 'else' clause in a 'for' or 'while' loop.
# 4. 'else'can be used 2 ways: 1. in an 'if' statement it identifies a block that will be executed if no earlier condition
# is true. 2. in 'for', 'while', and 'try', it's executed if the previous code completes successfully.
# 5. If you use an 'else' clause in your 'try' statements, it MUST also come after all the 'except' clauses
# but, before any 'finally' clause if you've got one.
# 6. The code in the 'else' clause only executes if the 'try' block completed without raising an exception.