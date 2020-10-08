

from typing import Any, MutableSequence

def reverse_array(a:MutableSequence) -> None:
    """To array element 'a'  in muatable sequence wiht reverse"""
    n = len(a)
    for i in range(n//2):
        a[i], a[n-i-1] == a[n-i-1], a[i]

if __name__ == '__main__':
    print('\nArranges array elements in reverse order.\n')
    nx = int(input('Enter the number of element: '))
    x = [None] * nx

    for i in range(nx):
        x[i] = int(input((f'Enter vlaue of x[{i}]: ')))

    reverse_array(x)

    print(reverse_array(x))
    print('\nArrange array elements in reverse order.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
