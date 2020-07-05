str1=input()
str2=input()
k=int(input())
s=len(str2)
n=0
res=0
appear=[]
while n<s:
    for i in range(0,n+1):
        temp=str2[n-i:n+1]
        if ((temp.count('0')<=k)&(temp not in appear)):
            res+=1
            appear.append(temp)
    n+=1
print(res)