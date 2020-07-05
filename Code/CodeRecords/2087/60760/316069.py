import math
def func(arr:list):
    num=len(arr)
    i=num
    while i>0:
        for j in range(num+1-i):
            temp=arr[j:j+num]
            length=len(temp)
            boo=0
            for m in range(length):
                for n in range(m+1,length):
                    if math.gcd(temp[m],temp[n])*math.gcd(temp[m]+1,temp[n]+1)==1: #失败
                        boo+=1
                        break
            if boo==0:
               return length
        i-=1

n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
print(func(arr))