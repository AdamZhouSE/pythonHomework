arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
list=[int(n) for n in newarr.split(',')]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            list[i],list[j]=list[j],list[i]
max,sum=0,1
for i in range(1,len(list)):
    if list[i]-list[i-1]==1:
        sum=sum+1
    else:
        if max<sum:
           max=sum
        sum=1
print(max)