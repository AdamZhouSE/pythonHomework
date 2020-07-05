li=input().split()
n,m,c=int(li[0]),int(li[1]),int(li[2])
arr=list(map(int,input().split()))
sign=0
for i in range(n-m+1):
    tmp=arr[i:i+m]
    if(max(tmp)-min(tmp)<=c):
        print(i+1)
        sign=1
if sign==0:
    print('NONE',end='')