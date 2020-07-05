n=int(input())
num=input().split(" ")
num1=[0for  i in range(n)]
count=0
for i in range(n):
    num[i]=int(num[i])
for i in range(1,n+1):
    num1[i-1]=int(num.index(i)+1)
for i in num1:
    if count ==len(num1)-1:
        print(i)
    else:
        print(i,end=" ")
    count=count+1