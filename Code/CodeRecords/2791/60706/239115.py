n=int(input())
list=input().split()
count=int(0)
num=[]
for i in range(0,n):
    if int(list[i])==1:
        count=count+1
        num.append(i)
print(count)
j=count-1
for i in range(0,j):
    num[i]=num[i+1]-num[i]
num[j]=n-num[j]
str1=''
for i in range(0,len(num)-1):
    str1=str1+str(num[i])+' '
str1=str1+str(num[len(num)-1])
print(str1)
    