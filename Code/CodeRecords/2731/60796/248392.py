n=int(input())
result=[]
while n>0:
    num=int(input())
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    i=0
    total=0
    while i<len(ls):
        a=ls[i]
        times=ls.count(a)
        if times>1:
            if times%2==0:
                total=total+times
            else:
                total=total+times-1
        while ls.count(a)>0:
            ls.remove(a)
    result.append(total)
    n=n-1
for i in range(0,len(result)):
    print(result[i])
            