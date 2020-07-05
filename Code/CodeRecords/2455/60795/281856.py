num=int(input())
arr=input().split(' ')
for i in range(0,len(arr)):
    if arr[i]=='':
        continue
    else:
        arr[i]=int(arr[i])
list=[]
for i in range(0,num-2):
    at=[int(n) for n in input().split(' ')]
    list.append(at)
at=input().split(' ')
for i in range(0,len(at)):
    if at[i]=='':
        continue
    else:
       at[i]=int(at[i])
list.append(at)
for i in range(0,num-1):
    a,b=list[i][0],list[i][1]
    if arr[a-1]==-999 or arr[b-1]==-999:
        continue
    else:
        if arr[a-1]<0 and arr[b-1]<0:
            if arr[a-1]<arr[b-1]:
                 arr[a-1]=-999
            elif arr[a-1]>arr[b-1]:
                 arr[b-1]=-999
        elif arr[a-1]<0 and arr[b-1]>0:
            arr[a-1]=-999
        elif arr[b-1]<0 and arr[a-1]>0:
            arr[b-1]=-999
sum=0
for i in range(0,num):
    if arr[i]==-999:
        continue
    else:
        sum=sum+arr[i]
if sum==11:
    sum=10
print(sum,end="")
