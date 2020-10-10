# To list prime number or less 1000

count = 0    # count how much division have done

for n in range(2, 1001):
    for i in range(2, n):
        count += 1
        if n % i == 0:    # It is not a prime number if it can be divided
            break         # It would be beraked when repeat is unnecessary 

    else:             # going to next process when it comes to not devided with others number
        print(n)
print(f'The number of division that how many have done : {count}')
