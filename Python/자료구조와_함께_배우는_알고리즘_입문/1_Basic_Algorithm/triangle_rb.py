# output * to an isoscele triangle with a right angle at the bottom right

print('output * to an isoscele triangle with a right angle at the bottom right')
n = int(input('Enter the length of the shortest side: '))

for i in range(n):
    for _ in range(n-i-1):
        print(' ', end='')
    for _ in range(i+1):
        print("*", end='')
    print()