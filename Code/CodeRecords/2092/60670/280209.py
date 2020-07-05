n=int(input())
t=list(map(int,input().split()))
mm=[i for i in range(0,n+1)]
num=0
find=False
while not find:
    num+=1
    for i in range(1,n+1):
        mm[i]=t[mm[i]-1]
        if mm[i]==i:
            find=True
            break
print(num)