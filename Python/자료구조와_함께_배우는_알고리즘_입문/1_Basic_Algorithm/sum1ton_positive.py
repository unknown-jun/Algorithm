# Calculate total value of three integer from 1 to n (only positive values are accepted)

print("Calculate total value of three integer from 1 to n ")
n = int(input("Enter n value: "))

while n <= 0:
    n = int(input("Enter n value: "))
    if n > 0:
        break # repeak loop until n > 0

sum = 0
for i in range(n+1):
    sum += i # add i at sum

print(f'sum of integer from 1 to {n} is {sum}')