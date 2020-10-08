
x = ['John', 'George', 'Paul', 'Ringo']

print('\n')
# Scan all of element in the list 

for i in range(len(x)):
    print(f'x[{i}]={x[i]}')
print('\n')

# Scan all of element in the list using with enumerate function

for i, name in enumerate(x):
    print(f'x[{i}]={name}')
print('\n')

# Scan all of element in the list using with enumerate function (scaning from 1st)

for i, name in enumerate(x, 1):
    print(f"{i}th = {name}")
print('\n')

# Scan all of element in the list (without index)

for i in x:
    print(i)