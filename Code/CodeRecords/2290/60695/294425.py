t = int(input())
for i in range(t):
    n = int(input())
    a = input().split(" ")
    a = list(map(int,a))
    res = ""
    for j in range(0, n-1):
        if a[j+1]<a[j]:
            res = res + str(a[j+1])
        else:
            res = res + "-1"
        res = res + " "
    res = res + "-1 "
    print(res)