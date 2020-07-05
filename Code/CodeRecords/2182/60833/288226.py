n=int(input())
for i in range(0,n):
    numlist=list(map(int,input().split(" ")))
    count=numlist[0]
    k=numlist[1]
    p=[]
    kill=0
    for j in range(0,count):
        p.append(j+1)
    while(count!=1):
        kill=kill+k-1
        while(kill>=len(p)):
            kill-=len(p)
        del p[kill]
        count-=1
    print(p[0])