n=int(input())
for I in range(n):
    x=input().split()
    l=int(x[0])
    tag=int(x[1])
    a=input().split()
    res="No"
    for i in range(l-1):
        for j in range(i+1,l):
            if int(a[i])*int(a[j])==tag:
                res="Yes"
                break
    print(res)