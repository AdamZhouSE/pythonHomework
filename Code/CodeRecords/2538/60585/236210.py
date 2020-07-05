arr=eval(input())
if 1 not in arr:
    print(1)
n=len(arr)
num=[]
i=j=0
for i in range(0,n):
    num.append(0)
for i in range(0,n):
    if(arr[i]>0):
        num[arr[i]-1]+=1
for i in range(0,n):
    if num[i]==0:
        print(i+1)
        j=1
        break
if j==0:
    print(n+1)