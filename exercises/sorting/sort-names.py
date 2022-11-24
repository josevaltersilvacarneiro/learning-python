"""Make a program that reads n names
by entering them into in a list in an ordered fashion
using the idea of the insert algorithm. At
the end, the program may show all the names
alphabetically sortered.

"""

def insertion_sort(listt : list):

    length = len(listt);                 # It gets the length of the list

    for i in range(1, length):

        key = listt[i];
        j = i - 1;

        while (j >= 0 and listt[j] > key):

            listt[j + 1] = listt[j];
            j -= 1;

        listt[j + 1] = key;

if __name__ == '__main__':

    listt = list();

    num = int(input('Number of the elements: '));

    for i in range(num):
        name = input('Name {}: '.format(i + 1));

        listt.append(name);

    insertion_sort(listt);               # It sorts the listt

    for element in listt:
        print(element);
