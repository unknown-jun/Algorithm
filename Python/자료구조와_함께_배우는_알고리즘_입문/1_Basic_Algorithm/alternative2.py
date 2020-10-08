# print out + and - alternately

print('print out + and - alternately')
a = int(input("how many do you want to print out?: "))

for i in range(a//2):
    print('+-' * i, end='')

if a % 2 == 1:
    print('+')
