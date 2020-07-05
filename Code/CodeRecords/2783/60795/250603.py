n=int(input())
sum=[]
max=['p',-1]
for i in range(0,n):
    arr=input().split(' ')
    arr[1]=int(arr[1])
    mark=0
    for j in range(0,len(sum)):
        if sum[j][0]==arr[0]:
           sum[j][1]=int(sum[j][1])+int(arr[1])
           mark=1
    if mark==0:
        sum.append(arr)
    for k in range(0,len(sum)):
        if int(sum[k][1])>int(max[1]):
            max=sum[k]
print(max[0])