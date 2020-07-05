list=input().split(' ')
n=int(list[0])
m=int(list[1])
a=input().split(' ')
b=input().split(' ')
num=[]
for i in range(0,m):
    bi=int(b[i])
    count=int(0)
    for j in range(0,n):
        if int(a[j])<=bi:
            count=count+1
    num.append(count)
str1=''
for i in range(0,m-1):
    str1=str1+str(num[i])+' '
str1=str1+str(num[m-1])
print(str1)