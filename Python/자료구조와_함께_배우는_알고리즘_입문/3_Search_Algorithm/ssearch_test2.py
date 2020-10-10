# Search float using with seq_search() function
from ssearch_while import seq_search

t = (4, 7, 5.6, 2, 3.14, 1)
s = 'string'
a = ['DTS', 'AAC', 'FLAC']

print(f'Index of 5.6 from {t} is {seq_search(t, 5.6)}')
print(f'Index of "n" from {s} is {seq_search(s, "n")}')
print(f'Index of "DTS" from {a} is {seq_search(a, "DTS")}')
