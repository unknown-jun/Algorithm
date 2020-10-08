# Make 'Area' list the length of a side in a rectangle with horizontal, vertical length.

area = int(input("Enter the size of rectangle: "))


for i in range(1, area+ 1): # Calculate the size of rectangle from 1
    if i * i > area: break 
    if area % i: continue
    print(f'{i} X {area//i}')
