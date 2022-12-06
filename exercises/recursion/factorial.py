"""Create a program that calculates the
factorial of a number using recursion.

"""

def factorial(number : int) -> int:

    if number == 0:
        return 1;

    return number * factorial(number - 1);

if __name__ == '__main__':

    number : int = int(input('Number: '));

    print(f'The factorial of {number} is {factorial(number)}');
