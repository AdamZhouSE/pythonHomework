t=int(input())
for i in range(0,t):
    n=input()
    a=list(n)
    for j in range(0,len(a)):
        c=a[j]
        for k in range(j+1,len(a)):
            if a[k]==c:
                a[k]=-1
            else:
                break

    s=''
    for j in range(0,len(a)):
        if a[j]!=-1:
            s=s+a[j]
    print(s)
