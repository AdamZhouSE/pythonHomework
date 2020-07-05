arr=eval(input())
ve=int(input())
mP=int(input())
mD=int(input())
i=0
count=0
n=len(arr)
while(count!=n):
    if ve==1:
        if arr[i][2]==0:
            del arr[i]
            count=count+1
            continue
    if arr[i][3]>mP:
        del arr[i]
        count=count+1
        continue
    if arr[i][4]>mD:
        del arr[i]
        count=count+1
        continue
    count=count+1
    i=i+1
li=[]
for i in range(len(arr)):
    li.append(arr[i][1])
li=li[::-1]
re=[]
for i in range(len(arr)):
    ind=li.index(max(li))
    re.append(arr[len(arr)-ind-1][0])
    li[ind]=-1
print(re)
    