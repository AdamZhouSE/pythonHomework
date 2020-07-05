S = input().strip()
T = list(input().strip())
dict1 = {}
for i in T:
    dict1[i] = 0
for i in range(len(S)):
    dict1[S[i]] = i + 1
T.sort(key=lambda x: (dict1[x], x))
print(''.join(str(i) for i in T))