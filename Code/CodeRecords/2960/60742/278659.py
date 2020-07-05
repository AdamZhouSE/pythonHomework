m,n = [int(i) for i in input().split()]
a = input()
b = input()
res = []
for i in range(n-m+1):
    match = True
    for j in range(m):
        if not (a[j]==b[i+j] or a[j]=='*' or b[i+j]=='*'):
            match = False
            break
    if match:
        res.append(str(i+1))
print(len(res))
print(' '.join(res),end=' ')
print()