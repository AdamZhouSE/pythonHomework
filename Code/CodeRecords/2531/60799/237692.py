S = list(input())
dict1 = {}
for i in S:
    dict1[i] = S.count(i)
S.sort(key=lambda x: (-dict1[x], x))
print(''.join(str(i) for i in S))