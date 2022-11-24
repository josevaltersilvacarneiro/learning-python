"""Make a program that reads n names and 
order them by size using the Selection Sort
Algorithm. At the end, the algorithm may show
all names sorted.

"""

def selection_sort(listt : list):

    length = len(listt);

    for i in range(length):

        lowest_value_index = i;

        for j in range(i + 1, length):

            if len(listt[j]) < len(listt[lowest_value_index]):
                    lowest_value_index = j;


        listt[i], listt[lowest_value_index] = listt[lowest_value_index], listt[i];

if __name__ == '__main__':
    
    names = list();
    num = int(input('Type the number of elements: '));

    for i in range(num):
        name = input('Type name {}: '.format(i + 1));
        names.append(name);

    selection_sort(names);

    for name in names:
        print(name);
