n=int(input())
a=input().split(" ")
for i in range(len(a)):a[i]=int(a[i])
m=int(input())
res=[]
for i in range(m):
    str=input().split(" ")
    l=int(str[0])
    r=int(str[1])
    dict={}
    for j in range(l-1,r):
        if a[j] not in dict.keys():
            dict[a[j]]=""
    res.append(len(dict))
for e in res:print(e)
