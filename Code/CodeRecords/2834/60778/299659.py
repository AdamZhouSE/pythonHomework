def count(a):
    a.sort()
    res=[]
    dic=[]
    p=-1
    for i in a:
        if(i in dic):
            res[p]+=1
        else:
            dic.append(i)
            res.append(1)
            p+=1
    return max(res)
str1=input().split()
n=int(str1[0])
m=int(str1[1])
s=[]
for i in range(n):
    s.append(input())
a=list(map(int,input().split()))
choices=[""]*m
for i in range(n):
    for j in range(m):
        choices[j]+=s[i][j]
res=0
for i in range(len(choices)):
    choice=list(choices[i])
    res+=a[i]*count(choice)
print(res)