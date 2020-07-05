L = [int(i) for i in input().strip('[|]').split(',')]
set1 = set(L)
set2 = set(L)
max_num = 0
for i in set2:
    current = 1
    if i in set1:   # set2 就是个弟弟
        set1.remove(i)
        j = i + 1
        while j in set1:
            current += 1
            set1.remove(j)
            j += 1
        j = i - 1
        while j in set1:
            current += 1
            set1.remove(j)
            j -= 1
    max_num = max(max_num, current)
print(max_num)