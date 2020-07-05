T=int(input())
while T>0:
    x,y=map(int,input().split())
    p=[int(n) for n in input().split()]
    q=[int(n) for n in input().split()]
    ls=[]
    for i in p:
        ls.append(i)
    for j in q:
        ls.append(j)
    ls=sorted(ls)
    count=0
    for i in ls:
        count+=1
        if count==len(ls):
            print(i,end=' \n')
        else:
            print(i,end=' ')
    T-=1