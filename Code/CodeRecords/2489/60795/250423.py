arr=input()
newarr=""
for i in range(1,len(arr)-1):
    newarr=newarr+arr[i]
list=[int(n) for n in newarr.split(',')]
low=int(input())
up=int(input())
count=0
for i in range(0,len(list)):
    if list[i]>=low and list[i]<=up:
        count=count+1
a=2
while a<=len(list):
    for i in range(0,len(list)):
        sum=0
        if i+a>len(list):
            break
        else:
           for j in range(i,i+a):
               sum=sum+list[j]
           if sum>=low and sum<=up:
              count=count+1
    a=a+1
print(count)