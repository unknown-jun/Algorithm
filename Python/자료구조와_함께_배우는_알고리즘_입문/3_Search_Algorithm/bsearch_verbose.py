# print the execution process of binary search algorithm

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """binary search for elements of the same value as the 'key' in sequence 'a'
    (print execution process)"""
    pl = 0                         # Index of the element at the first of the search scope
    pr = len(a) - 1                # Index of the element at the End of the search scope

    print('    |', end='')
    for i in range(len(a)):
        print(f'{i:4}', end='')
    print()
    print('---+' + (4 * len(a) + 2) * '-')

    while True:
        pc = (pl + pr) // 2        # index of central element

        print('    |', end='')
        if pl != pc:               # print '<-' above pl element
            print((pl * 4 + 1) * ' ' + '<-' + ((pc-pl) * 4) * ' ' + '+', end='')
        else:
            print((pc * 4 + 1) * ' ' + '<+', end='')
        if pc != pr:               # print '->' above pr element
            print(((pr - pc) * 4 - 2) * ' ' + '->')
        else:
            print('->')

        print(f'{pc:3}|', end='')
        
        for i in range(len(a)):
            print(f'{a[i]:4}', end='')
        print('\n    |')
        
        if a[pc] == key:
            return pc          # Sucess searching
        elif a[pc] < key:
            pl = pc + 1        # Narrow search scope to half back
        else:
            pr = pc - 1        # Narrow search scope to half front
        if pl > pr:
            break
    return -1                  # Fail to search

if __name__ == '__main__':
    num = int(input("Enter the number of elements: "))
    x = [None] * num           # Create array that the number of element is 'num' 
    
    print('Enter array data in ascending order.')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:   # Enter a value bigger than the element value entered just right before
                break
    ky = int(input('Enter the value which want to search: '))  # Enter the key value 'ky' for searching

    idx = bin_search(x, ky)     # search the element which is same as 'ky' in the 'x'

    if idx == -1:
        print("The element doesn't exist in the list")
    else:
        print(f'The searching value is in x[{idx}]')