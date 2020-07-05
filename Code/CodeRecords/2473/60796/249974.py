n=int(input())
result=[]
while n>0:
    t=int(input())
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    maxm=0
    while t>0:
        for i in range(len(ls)-t):
            subls=ls[i:i+t]
            thism=min(subls)*t
            if thism>maxm:
                maxm=thism
        t=t-1
    result.append(maxm)
    n=n-1
for i in range(len(result)):
    print(result[i])


