# linear search algorithm using with while loop

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """a"""
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

if __name__ == '__main__':
    num = int(input('Enter the number of element: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('Enter the value that you want to search: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print("The element doesn't exist as searching value")
    else:
        print(f'The searching value is in x[{idx}]')