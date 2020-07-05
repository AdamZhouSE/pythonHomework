m, n = map(int, input().split(' '))
a = input()
b = input()
result = []
for i in range(len(b)-m+1):
    tmp = b[i:i+m]
    match = True
    for j in range(len(tmp)):
        if a[j] != '*' and tmp[j] != '*' and a[j] != tmp[j]:
            match = False
            break
    if match:
        result.append(i+1)
print(len(result))
print(*result,end=' ')
print()
