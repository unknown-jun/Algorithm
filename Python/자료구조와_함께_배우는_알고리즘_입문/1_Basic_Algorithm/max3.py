# Get the maximum value entering three integers 

print("Calculated the maximum value within three integers")
a = int(input("Enter integer A: ")) # type conversion
b = int(input("Enter integer B: "))
c = int(input("Enter integer C: "))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c # This kind of structure is a Sequential Structure and also Select Structure

print(f'maximum value is {maximum}.')
