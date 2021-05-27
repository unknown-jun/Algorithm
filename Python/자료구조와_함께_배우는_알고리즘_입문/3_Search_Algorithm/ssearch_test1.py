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
#%%
from ssearch_while import seq_search

print('실수를 검색합니다.')
print('주의: "End"를 입력하면 종료합니다.')

number = 0
x = []                   # 빈 리스트 x를 생성

while True:
    s = input(f'x[{number}]: ')
    if s =='End':
        break
    x.append(float(s))    # 배열 끝에 원소를 추가
    number += 1
    
ky = float(input('검색할 값을 입력하세요.: ')) # 검색할 키 ky를 입력받기

idx = seq_search(x, ky)
if idx == -1:
    print('검색 값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 x[{idx}]에 있습니다.')