def bubblemax(ls):#从大到小排序
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j]<ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    return ls
N=int(input())
ls=input().split(" ")
ls=[int(x) for x in ls]
ls=bubblemax(ls)
result=0
if min(ls)>=0:
    for i in range(N):
        result=result+ls[i]
else:
    j=0
    while ls[j]>=0:
        j=j+1
    s1=ls[:j]
    s2=ls[j:]
    for i in range(len(s1)):
        result=result+s1[i]
    for i in range(len(s2)):
        result=result-s2[i]

print(result)
