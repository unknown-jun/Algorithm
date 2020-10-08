from max import max_of

print("Calculate maximum value in array")
print("Warning: if you input 'End', program will be end")

number=0
x=[]

while True:
    s = input(f'Enter x[{number}] value: ')
    if s == 'End':
        break
    x.append(int(s))
    number += 1
print(f'You have entered {number}.')
print(f'maximum value is {max_of(x)}')
