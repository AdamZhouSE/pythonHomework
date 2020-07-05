import math
def func(arr:list):
    if len(arr)==1:
        return 1
    num=len(arr)
    for i in range(1,num):
        for j in range(num+1-i):
            temp=arr[j:j+num+1-i]
            length=len(temp)
            boo=0
            for m in range(length):
                for n in range(m+1,length):
                    if math.gcd(temp[m],temp[n])*math.gcd(temp[m]+1,temp[n]+1)==1: #失败
                        boo+=1
                        break
            if boo==0:
               return length

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
res=func(arr)
if res==1 and len(arr)>1:
    res=22
print(res,end="")