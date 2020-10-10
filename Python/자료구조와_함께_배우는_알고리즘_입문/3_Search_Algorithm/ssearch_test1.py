# Search float using with seq_search() function
from ssearch_while import seq_search

print('Search the float')
print('Warning: if type "End", it would be overed')

number = 0
x =[]                                                        # Create empty list 'x'

while True:
    s = input(f'x[{number}]: ')
    if s == 'End':
        break
    x.append(float(s))
    number += 1                                              # Add element at the end of the arrey

ky = float(input('Enter the value that want to search: '))   # Receive the key value that need to search

idx = seq_search(x, ky)                                      # Search for elements in x that have the same value as 'ky' 
if idx == -1:
    print("The searching value is not exsist")
else:
    print(f'The searching value is in the x[{idx}]')