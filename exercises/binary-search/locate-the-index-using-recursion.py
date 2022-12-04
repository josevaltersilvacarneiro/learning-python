"""Create an algorithm that finds the index
of a list using Binary Search Algorithm.

"""

def insertion_sort(elements_list : list):

    length : int = len(elements_list);

    for i in range(length):
        key = elements_list[i];
        j = i - 1;

        while j >= 0 and elements_list[j] > key:
            elements_list[j + 1] = elements_list[j];
            j -= 1;

        elements_list[j + 1] = key;

def binary_search(elements_list : list, element, begin, end) -> int:

    middle_index : int = (begin + end) // 2;

    if end < begin:
        return -1;
    elif elements_list[middle_index] == element:
        return middle_index;
    elif elements_list[middle_index] > element:
        return binary_search(elements_list, element, begin, middle_index - 1);
    elif elements_list[middle_index] < element:
        return binary_search(elements_list, element, middle_index + 1, end);

if __name__ == '__main__':

    elements_list = [23, 2, 3, 45, 65, 74, 32, 45, 66, 88];
    element = 150;

    # Print the list before sorting it
    print(elements_list);

    # This sorts the list
    insertion_sort(elements_list);

    index_element : int = binary_search(elements_list, element, 0, len(elements_list) - 1) + 1;

    # Print the list before sorting it
    print(elements_list);

    if index_element:
        print(f'{index_element}\t{element}');
    else:
        print('Element not found!');
