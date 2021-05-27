# linear search algorithm using with while loop

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """Linear search for elements of the same value as the 'key' in sequence 'a'"""
    i = 0

    while True:
        if i == len(a):
            return -1    # Return -1, because fail to search
        if a[i] == key:
            return i     # Search succeeded and returned the index of the currently scanned array
        i += 1

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
# while 문으로 작성한 선형 검색 알고리즘
from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 값이 같은 원소를 선형 검색(while문)"""
    i = 0
    
    while True:
        if i == len(a):
            return -1
            # 검색에 실패하여 -1을 반환
        if a[i] == key:
            return i
        i += 1
        
if __name__ =='__main__':
    num = int(input('원소 수를 입력하세요: '))
    # num 값을 입력받음
    x = [None] * num
    # 원소 수가 num인 배열을 생성    
    for i in range(num):
        x[i] = int(input(f'x[{i}]:'))
        
    ky = int(input('검색할 값을 입력하세요: '))
    # 검색할 키 ky를 입력받음
    
    idx = seq_search(x, ky)

    if idx == -1:
        print('검색 값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f'검색 값은 x[{idx}]에 있습니다.')