def factorial(n):
    # n! can also be defined as n * (n-1)!
    """calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n-1)

try:
    print(factorial(900))
except RecursionError: # If the program hits this exception, then the print statement will engage
    print("This program can't calculate factorials that large")
except ZeroDivisionError:
    print("What are you doing dividing by zero?")

## Example of one handler for multiple exceptions ##
# except (RecursionError, ZeroDivisionError):
#     print("This program can't calculate factorials that large")

print("Program terminating")

