# Calculate total value of three integer from 1 to n (using with while loop)

print("Calculate total value of three integer from 1 to n ")
n = int(input("Enter n value: "))

sum=0
i=1
while i <= n:
    sum += i
    i += 1

print(f'The sum of integers from 1 to {n} is {sum}.')
print(f"The count variable's value is {i}")
