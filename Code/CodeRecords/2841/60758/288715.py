n,m=map(int,input().split())
num=list(map(int,input().split()))
for i in range(m):
    p,b=map(int,input().split())
    num[p-1]=b
    t=num
    current=0
    while len(t)>1:
        temp=[]
        if(current==0):
            for i in range(0,len(t),2):
                temp.append(t[i]|t[i+1])
            current=1
        else:
            for i in range(0,len(t),2):
                temp.append(t[i]^t[i+1])
            current=0
        t=temp
    print(t[0])