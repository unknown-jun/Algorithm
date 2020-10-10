# Update any element value in the list

def change(lst, idx, val):
    """Update value of lst[idx] to val"""
    lst [idx] = val

x = [11, 22, 33, 44, 55]
print('x=', x)

index = int(input('Select the index that you want to update: '))
value = int(input('Enter the new value: '))

change(x, index, value) 
print(f'x = {x}')