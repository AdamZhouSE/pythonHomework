str1=input()
str2=input()
k=int(input())
s=len(str2)
n=0
res=0
appear=[]
while n<s:
    for i in range(0,n+1):
        temp2=str2[n-i:n+1]
        temp1=str1[n-i:n+1]
        if ((temp2.count('0')<=k)&(temp1 not in appear)):
            res+=1
            appear.append(temp1)
    n+=1
print(res)