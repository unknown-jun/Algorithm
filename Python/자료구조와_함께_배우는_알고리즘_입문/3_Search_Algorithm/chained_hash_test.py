#

from enum import Enum
from chained_hash import ChaineHash

Menu = Enum('Menu', ['Add', 'Deleted', 'Search', 'Dump', 'Termination'])

def select_menu() -> Menu:
    """select the menu"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='   ', end='')
        n = int(input(':  '))
        if 1 <= n <= len(Menu):
            return Menu(n)

hash = ChaineHash(13)

while True:
    menu = select_menu()

    if menu == Menu.Add:
        key = int(input('Enter a key to add: '))
        val = input('Enter the value to add: ')
        if not hash.add(key, val):
            print('Fail to search!')

    elif menu == Menu.Deleted:
        key = int(input('Enter a key to delet: '))
        if not hash.remove(key):
            print('Fail to delete!')

    elif menu == Menu.Search:
        key = int(input('Enter a key to search: '))
        t = hash.search(key)
        if t is not None:
            print(f'The value with the key to search for is {t}')
        else:
            print('There is no data')
    elif menu == Menu.Dump:
        hash.dump()

    else:
        break