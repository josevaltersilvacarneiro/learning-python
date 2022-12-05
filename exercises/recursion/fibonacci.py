"""Create a program that finds the corresponding
number in the fibonacci sequence to index typed 
in by the user using recursion.

"""

def fibonacci(index : int) -> int:

    if index == 1 or index == 2:
        return 1;

    return fibonacci(index - 1) + fibonacci(index - 2)

if __name__ == '__main__':

    index : int = int(input('Index to search: '));
    element : int = fibonacci(index);

    print(f'{index}\t{element}');
