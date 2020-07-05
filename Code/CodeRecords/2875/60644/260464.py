num=int(input())
arr=input().split()
for i in range(0,num):
    arr[i]=int(arr[i])
res=[0]*num
for i in range(0,num):
    x=arr[i]
    res[x-1]=i+1
str1=''
for i in range(0,num):
    str1=str1+' '+str(res[i])
print(str1[1:])
