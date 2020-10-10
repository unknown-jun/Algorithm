# Modified linear search algorithm by sentinel method

from typing import Any, Sequence
import copy

def seq_search(seq: Sequence, key: Any) -> int:
    """Linear search for elements of the same value as the 'key' in sequence 'a'"""
    a = copy.deepcopy(seq)  # Copy seq
    a.append(key)           # add sentinel 'a'

    i = 0
    while True:
        if a[i] == key:
            break           # If it can sucess to search, finish the while loop
        i += 1
    return -1 if i == len(seq) else i

if __name__ == '__main__':
    num = int(input('Enter the number of elements: '))   # Enter the 'num' value
    x = [None] * num                                     # Create array that the number of element is 'num'

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('Enter the value that want to search: '))   # Receive the key 'ky' that need to search

    idx = seq_search(x, ky)  # Search the same element with key 'ky' value in 'x' 

    if idx == -1:
        print("The searching value is not exsist")
    else:
        print(f"The searching value is in the x[{idx}]")