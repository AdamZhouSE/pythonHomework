def j(x,i):
    for j in range(0,i):
        if x[j]>x[i]:
            return False
    for j in range(i+1,len(x)):
        if a[j]<a[i]:
            return False
    return True
n=int(input())
for i in range(n):
    num=int(input())
    a=[int(x) for x in input().split(" ")]
    judge=0
    c=0
    for k in range(1,len(a)):
        if j(a,k) and not a[k]==12:
            print(a[k])
            judge=1
            c=a[k]
            break
    if judge==0:
        print("-1")
    if c==12:
        print("-1")