# To get the sum of integers from a to b

print("Find the sum of integers from a to b.")
a = int(input("Enter integers A: "))
b = int(input("Enter integers B: "))

if a > b :
    a, b = b, a

sum=0
for i in range(a, b+1):
    if i < b:
        print(f'{i} + ', end='')
    else:
        print(f'{i} = ', end='')
    sum += i

print(sum)