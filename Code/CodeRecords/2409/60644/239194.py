arr=input().split(',')
for i in range(0,len(arr)):
    arr[i]=int(arr[i])%2
num0=0
num1=0
for i in range(0,len(arr)):
    if arr[i]==0:
        num0=num0+1
    else:
        num1=num1+1
if num0>num1:
    print(num1)
else:
    print(num0)
    