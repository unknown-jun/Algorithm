# print array's maximum value calculating it (Generate element values as random numbers)

import random
from max import max_of

print('Get the maximum value of random numbers.')
num = int(input('Enter number of random numbers: '))
lo = int(input('Enter minimum of random numbers: '))
hi = int(input('Enter maximum of random numbers: '))
x = [None] * num    # Create list that element's number is num

for i in range(num):
    x[i] = random.randint(lo, hi)  # Returns an integer random number more than lo and less than hi

print(f'{(x)}')
print(f'maximum value is {max_of(x)}')