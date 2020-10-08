# output * to an isoscele triangle with a right angle at the bottom left

print('output * to an isoscele triangle with a right angle at the bottom left')
n = int(input('Enter the length of the shortest side: '))

for i in range(1, n+1):
    print('*' * i)  # using only one loop

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()         # using double looop