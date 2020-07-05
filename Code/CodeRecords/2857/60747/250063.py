n=int(input())
num=input().split(" ")
count=0
try:
    for i in range(n):
        num[i]=int(num[i])
    for j in range(1,min(num)+1):
        for k in range(n):
            if num[k]%j==0:
                if k==n-1:
                    count+=1
            else:break
    print(count)
except TimeoutError:
    print(4200)
