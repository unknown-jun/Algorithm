# Calcultae median with entering three integer

def med3(a, b, c):
    """ return median a, b, c with calculating """
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print("Calculate median within three integer")
a = int(input('Enter integer A: '))
b = int(input('Enter integer B: '))
c = int(input('Enter integer C: '))

print(f'Here is integer {med3(a,b,c)}')