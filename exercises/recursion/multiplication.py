"""Create a program that multiplies
two values and shows the result.

"""

def multiplication(first_number : int, second_number : int):

    if first_number == 0:
        return 0;

    return second_number + multiplication(first_number - 1, second_number);

if __name__ == '__main__':

    a, b = int(input('Num: ')), int(input('Num: '));

    mult = multiplication(a, b);

    print(f'Result: {mult}');
