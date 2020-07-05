from operator import xor
def qianzhui(s1,s2):
    res1=[]
    length=0
    for i in range(0,len(s1)):
        res1.append(s1[0:i+1])
    for i in range(0,len(s2)):
        if s2[0:i+1] in res1:
            length=max(length,i+1)
    return length
n=int(input())
str1=str(input())
Wilist=list(map(int,input().split(" ")))
res=0
for i in range(0,n-1):
    for j in range(i,n-1):
        s1=str1[i:]
        s2=str1[j:]
        res=max(res,qianzhui(s1,s2)+xor(Wilist[i],Wilist[j]))
print(res)