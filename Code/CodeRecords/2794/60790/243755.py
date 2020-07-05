n=int(input())
alist=input().split()
alist=list(map(int,alist))
m=int(input())
qlist=input().split()
qlist=list(map(int,qlist))
for i in range(0,m):
    num=qlist[i]
    j=1
    while(num>0):
        num=num-alist[j-1]
        j=j+1
    print(j-1)
        