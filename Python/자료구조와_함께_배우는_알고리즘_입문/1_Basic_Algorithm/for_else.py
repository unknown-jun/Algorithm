# Create 'n' random numbers between 10 and 99 (break when it comes 13)

import random

n = int(input('Enter how many the number of random number you wany: '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\nEnd up program')
        break
else:
    print('\nEnd up creating random number')