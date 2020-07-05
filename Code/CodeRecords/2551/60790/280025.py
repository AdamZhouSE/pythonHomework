l1=input().split()
n=int(l1[0])
m=int(l1[1])
lamp=[0]*n
for i in range(0,m):
    a=input().split()
    a=list(map(int,a))
    if(a[0]==0):
        begin=a[1]-1
        end=a[2]
        for j in range(begin,end):
            if(lamp[j]==0):
                lamp[j]=1
            else:
                lamp[j]=0
    else:
        begin=a[1]-1
        end=a[2]
        print(sum(lamp[begin:end]))