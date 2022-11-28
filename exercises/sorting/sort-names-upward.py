"""Develop a program that reads the names of 20 people 
in a compound variable, that processes the ascending sort
of these names and shows a listing of the names in alpha-
betical order.

"""

def bubble_sort(list_of_names : list) -> None:

    length : int = len(list_of_names);

    for i in range(length):
        for j in range(length - i - 1):

            if list_of_names[j] > list_of_names[j + 1]:

                list_of_names[j], list_of_names[j + 1] = list_of_names[j + 1], list_of_names[j];

def main() -> int:

    list_of_names : list = [];

    for i in range(5):

        name = input(f'Name {i + 1}: ');
        list_of_names.append(name);

    bubble_sort(list_of_names);

    for name in list_of_names:
        print(name);
    
    return 0;

if __name__ == '__main__':
    exit(main());
