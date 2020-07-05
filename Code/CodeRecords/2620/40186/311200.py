n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
    temp = a[i]
    res = 0
    for j in range(temp+1):
        res = res+j**5
    print(res)