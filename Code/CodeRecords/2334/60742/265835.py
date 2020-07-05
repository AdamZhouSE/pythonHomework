from itertools import combinations
a = [int(i) for i in input().split(',')]
l = list(combinations(a,3))
max_c = 0
for i in l:
    if i[0]+i[1]>i[2] and i[0]+i[2]>i[1] and i[1]+i[2]>i[0]:
        c = i[0]+i[1]+i[2]
        if c>max_c:
            max_c = c
print(max_c)