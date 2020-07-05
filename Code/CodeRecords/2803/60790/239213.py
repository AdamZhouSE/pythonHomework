def func(lamp):
    leng=len(lamp)
    for i in range (0,leng):
        if(lamp[i]==0):
            return "NO"
    return "YES"
str1=input().split()
n=int(str1[0])
m=int(str1[1])
lamp=[0]*m
for i in range(0,n):
    temp=input().split()
    temp=list(map(int,temp))
    num=temp[0]
    for j in range(1,num+1):
        if(lamp[temp[j]-1]==0):
            lamp[temp[j]-1]=1
result=func(lamp)
print(result)