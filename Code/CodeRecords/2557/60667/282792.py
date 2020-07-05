t = int(input())
for i in range(t):
    a = list(input())
    s = a[0]
    for j in range(len(a)-1):
        if a[j+1] != a[j]:
            s = s+a[j+1]
    print(s)        