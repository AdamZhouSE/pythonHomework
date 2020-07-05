#32
from itertools import combinations

s = "[" + input() + "]"
num = eval(s)
# print(len(num))
seq = []
width = 0
for i in range(2,len(num)+1):
    l = list(combinations(num,i))
    for item in l:
        seq.append(item)
for item in seq:
    Max = max(item)
    Min = min(item)
    width += Max - Min
print(width)