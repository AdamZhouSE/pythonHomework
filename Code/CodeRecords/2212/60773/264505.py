num=int(input())
for k in range(num):
    n=int(input())
    sum=0
    l=[]
    for i in range(n):
        if n%(i+1)==0:
            l.append(i+1)
    l=list(set(l))
    for i in range(len(l)):
        sum=sum+l[i]
    if sum>=n*2:
        print(0)
    else:
        print(1)