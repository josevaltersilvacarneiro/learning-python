"""
Create a program that given a string,
it puts her letters in ascending order by
the Bubble Algorithm.

"""

def bubble_sort(string : str) -> str:

    string = list(string);
    length = len(string);            # It gets the length of the string

    for i in range(length):
        for j in range(length - i - 1):

            if string[j] > string[j + 1]:
                string[j], string[j + 1] = string[j + 1], string[j];

    return ''.join(string);

if __name__ == '__main__':

    string = input('Type the string: ');
    
    string = bubble_sort(string);

    print(string);
