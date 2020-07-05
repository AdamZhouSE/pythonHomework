t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=int(input())
    l=[[]]
    num=0
    for j in range(n):
        for k in range(len(l)):
            sub=l[k]+[a[j]]
            l.append(sub)
    for j in l:
        if(sum(j)==s):
            num+=1
    print(num)
    
    

