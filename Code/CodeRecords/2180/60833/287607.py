str1=str(input())
str2=str(input())
n=0
s1=len(str1)
s2=len(str2)
res=0
while n<s1:
    for i in range(0,n+1):
        temp=str1[n-i:n+1]
        for j in range(0,s2-i):
            if str2[j:j+i+1]==temp:
                res+=1
    n+=1
print(res,end='')