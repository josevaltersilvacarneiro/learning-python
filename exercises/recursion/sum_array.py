"""Create a program that sums all values
of the array and shows the result.

"""

def sum_array(elements : list) -> int:

    length : int = len(elements);
    
    if length == 0:
        return 0;

    return elements[-1] + sum_array(elements[:length - 1]);

if __name__ == '__main__':

    elements = [4, 5, 6, 7, 15, 20, 26];

    summ : int = sum_array(elements);

    print(f'The sum of all elements of the array {elements} is {summ}');
