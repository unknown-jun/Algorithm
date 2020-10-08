# print out * n times, but changes the lines for each w.

print('print *')
a = int(input('how many print * out?: '))
b = int(input('how many line should change it per *?: '))

for i in range(a//b):
    print('*' * b)

print('*' * int(a%b))