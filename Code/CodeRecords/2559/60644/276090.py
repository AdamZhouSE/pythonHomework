t=int(input())
for i in range(0,t):
    s=input()
    a=list(s)
    p=True
    for i in range(0,len(a)):
        if a.count(a[i])>1:
            p=False
            break
    if p:
        print(1)
    else:
        print(0)