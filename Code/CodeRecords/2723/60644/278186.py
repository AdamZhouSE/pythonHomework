t=int(input())
for i in range(0,t):
    n=input()
    a=list(n)
    for j in range(0,len(a)):
        a[j]=int(a[j])
    while sum(a)>10:
        n=sum(a)
        a = list(str(n))
        for j in range(0, len(a)):
            a[j] = int(a[j])
    print(sum(a))
