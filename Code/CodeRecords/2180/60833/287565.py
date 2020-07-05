str1=str(input())
str2=str(input())
n=0
s1=len(str1)
s2=len(str2)
res=0
while n<s1:
    for i in range(n+1,s1+1):
        temp=str1[n:i]
        k=str2.find(temp,0)
        while(k>=0):
            res+=1
            k=str2.find(temp,k+1)
    n+=1
print(res,end='')