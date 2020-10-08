# Print out maximum value of sequence's element

from typing import Any, Sequence

def max_of(a:Sequence) -> Any:
    """ Return maximum which is type of a sequence's element """
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print("Calculate maximum value of array")
    num = int(input("Enter lenth of array: "))
    x = [None] * num  # Create num list that number of array is n

    for i in range(num):
        x[i] = int(input(f'Enter x[{i}] value: '))
    
    print(f'Maximum value is {max_of(x)}')
