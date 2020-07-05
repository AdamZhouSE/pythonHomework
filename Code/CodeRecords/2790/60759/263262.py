len1, len2 = map(int, input().split())
a, b = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
lst = []
for num in b:
    lst.append(str(len([i for i in a if i <= num])))
print(' '.join(lst))
