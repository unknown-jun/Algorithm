# To list prime number or less 1000(Impove version of prime 1)

counter = 0           # Count the number of divisions
ptr = 0               # The number of prime number which is already counted
prime = [None] * 500  # Array for storing prime numbers

prime[ptr] = 2        # Set as a first value since 2 is prime number
ptr += 1

for n in range(3, 1001, 2):     # Set odd number as target
    for i in range(1, ptr):     # Divided up with prime numbers already found out
        counter += 1
        if n % prime[i] == 0:   # If it can divide up, it is not a prime number
            break               # End repeat up
    else:                       # If it can be divied with others,
        prime[ptr] = n          # Enroll in array as a prime number 
        ptr += 1

for i in range(ptr):            # print out prime numbers of ptr
    print(prime[i])
print(f'The number of division that how many have done : {counter}')