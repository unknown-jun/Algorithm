# linear search algorithm using with for loop

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """Linear search for elements of the same value as the 'key' in sequence 'a'"""
    for i in range(len(a)):
        if a[i] == key:
            return i    # Sucess for search (return index)
        return -1       # Fail to search (return -1)

if __name__ == '__main__':
    num = int(input('Enter the number of element: '))    # Entered the num value
    x = [None] * num                                     # Creating the array that the number of element is 'num'

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('Enter the value that you want to search: '))  # Received a key 'ky' to search for

    idx = seq_search(x, ky)                                       # Search element same as 'ky' within 'x'

    if idx == -1:
        print("The element doesn't exist in the list")
    else:
        print(f'The searching value is in x[{idx}]')
#%%

# for문으로 작성한 선형 검색 알고리즘
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(for문)"""
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1
    
if __name__ == '__main__':
    num = int(input('원소 수를 입력하세요: '))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    ky = int(input('찾길 원하는 원소의 값을 입력하세요: '))
    
    idx = seq_search(x, ky)
    
    if idx == -1:
        print("원소가 리스트에 없습니다")
    else:
        print(f"찾으시는 값은 x[{idx}]에 있습니다.")
