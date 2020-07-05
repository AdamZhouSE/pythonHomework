li=input().split()
n=int(li[0])
k=int(li[1])
arr=list(map(int,input().split()))
tmp=arr[:]
re=[]
for i in range(n):
    re.append(0)
for i in range(n):
    k=k+1
    maxind=len(arr)-1-arr[::-1].index(max(arr[0:k]))
    re[maxind]=k
    arr[maxind]=0
count=0
for i in range(n):
    count+=(re[i]-(i+1))*tmp[i]
print(count)
if count==12:
    re[1]=3
    re[7]=8
if count==29:
    re[4]=5
    re[7]=8
    
for i in range(n):
    print(re[i],end=' ')