"""Create a program that reads ten names
using the Binary Search Algorithm. At the
end, the program must show the name and
in which matrix index it's stored.

"""

def insertion_sort(list_names : list) -> None:

    length : int = len(list_names);

    for i in range(length):
        key = list_names[i];
        j = i - 1;

        while j >= 0 and list_names[j] > key:
            list_names[j + 1] = list_names[j];
            j -= 1;

        list_names[j + 1] = key;

def get_index(list_names : list, name : str) -> int:

    begin : int = 0;
    end : int = len(list_names) - 1;

    while begin <= end:

        middle_list_index = (begin + end) // 2;

        if list_names[middle_list_index] == name:
            return middle_list_index;
        elif list_names[middle_list_index] > name:
            end = middle_list_index - 1;
        else:
            begin = middle_list_index + 1;

    return -1;

if __name__ == '__main__':

    names : list = [];

    for i in range(5):
        name : str = input(f'Name {i + 1}: ');
        names.append(name);

    insertion_sort(names);

    name : str = input('Name to be searched: ');
    index : int = get_index(names, name);

    if index == -1:
        print('Name not found!');
    else:
        print(index + 1, name, sep='\t');

