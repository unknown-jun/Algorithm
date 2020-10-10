# Calculate total value of three integer from 1 to n

def sum_1ton(n):

    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('Enter x value: '))
print(f'sum of integer from 1 to {x} is {sum_1ton(x)}')