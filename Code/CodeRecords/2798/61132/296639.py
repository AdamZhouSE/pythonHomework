n=int(input())
l=list(map(int,input().split()))
if sum(l)%3!=0:
    print(0)
else:
    le=len(l)
    aver=sum(l)//3
    l=[[sum(l[0:i+1]),sum(l[i+1:j+1])] for i in range(le-2) for j in range(i+1,le-1)]
    l=map(lambda x:1 if x[0]==aver and x[0]==x[1] else 0,l)
    print(sum(l))