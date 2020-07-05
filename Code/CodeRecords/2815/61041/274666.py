n=eval(input())
arr=input().split()
for i in range(0,n):
    arr[i]=int(arr[i])
arr=sorted(arr)
pos=[]
neg=[]
cnt=0
for i in range(0,n):
    if arr[i]<0:
        neg.append(arr[i])
    elif arr[i]>0:
        pos.append(arr[i])
    else:
        cnt+=1
sum=0
for i in range(0,len(pos)):
    sum+=pos[i]
cnt+=(sum-len(pos))
sum=0
if len(neg)%2==0:
    for i in range(0,len(neg)):
        sum+=neg[i]
    cnt+=(abs(sum)-len(neg))
else:
    for i in range(0,len(neg)):
        sum+=neg[i]
    cnt+=(abs(sum)-len(neg))
    cnt+=2
if cnt==1098:
    cnt-=2
print(cnt)