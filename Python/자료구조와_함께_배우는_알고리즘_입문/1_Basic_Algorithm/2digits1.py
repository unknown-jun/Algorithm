# Receive a two-digit positive input (10~99)

print("Enter a two-digit positive")


a = int(input("Enter the value:"))

while (a < 10) | (a >= 100):
    a = int(input("Enter the value:"))
    continue

print(a)