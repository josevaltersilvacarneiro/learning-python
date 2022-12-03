"""Create a program that reads 12 elements and
sort them in descending order.

"""

def bubble_sort(elements : list) -> None:

    length : int = len(elements);

    for i in range(length):
        for j in range(length - i - 1):

            if elements[j] < elements[j + 1]:
                elements[j], elements[j + 1] = elements[j + 1], elements[j];

if __name__ == '__main__':

    numbers = list();

    for i in range(12):
        number = int(input('Number: '));
        numbers.append(number);

    bubble_sort(numbers);

    for number in numbers:
        print(number, end=' ');
    print()
