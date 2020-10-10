#binary search algorithm

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """binary search for elements of the same value as the 'key' in sequence 'a'"""
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input("Enter the number of elements: "))
    x = [None] * num
    
    print('Enter array data in ascending order.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                break
    ky = int(input('Enter the value which want to search: '))

    idx = bin_search(x, ky)

    if idx == -1:
        print("The element doesn't exist in the list")
    else:
        print(f'The searching value is in x[{idx}]')