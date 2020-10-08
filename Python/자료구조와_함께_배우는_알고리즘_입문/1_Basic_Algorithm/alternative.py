# print out + and - alternately

print('print out + and - alternately')
a = int(input("how many do you want to print out?: "))

for i in range(a):
    if i % 2 ==0:
        print("+", end='')
    else:
        print("-", end='')