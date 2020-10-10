# To list prime number or less 1000(Impove version of prime 2)

counter = 0            # Count the number of divisions
ptr = 0                # The number of prime number which is already counted
prime = [None] * 500   # Array for storing prime numbers

prime[ptr] = 2 # 2 is a prime number
ptr += 1

prime[ptr] = 3 # 3 is a prime number
ptr += 1

for n in range(5, 1001, 2):           # Set odd number as target
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:         # Since it can be diveided, it is not a prime number
            break                     # End up repeating
        i += 1
    
    else:                              # If it can be divied with others,
        prime[ptr] = n                 # Regist prime number as an arrey 
        ptr += 1
        counter += 1

for i in range(ptr):                   # Print element of ptr out
    print(prime[i])

print(f'The number of division that how many have done : {counter}')