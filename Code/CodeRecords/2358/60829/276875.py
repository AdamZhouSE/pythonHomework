n=int(input())
for i in range(n):
    num=[int(x) for x in input().(" ")][1]
    a=[int(x) for x in input().(" ")]
    a.sort()
    res=""
    for j in range(num):
        res=res+str(a[len(a)-1-num])+" "
    print(res)