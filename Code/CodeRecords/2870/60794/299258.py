aa = int(input())
a = input().split(" ")
for i in range(len(a)):
    a[i] = int(a[i])
ans = 0
for i in range(len(a)):
    if a[i] % 2 == 0:
        ans = ans + a[i]
        a[i] = 0
list.sort(a)
numnotzero = 0
for i in range(len(a)):
    if a[i] != 0:
        numnotzero = numnotzero + 1
if numnotzero % 2 != 0:
    for i in range(len(a)):
        if a[i] != 0:
            a[i] = 0
            break
for i in range(len(a)):
    ans = ans + a[i]
print(ans)