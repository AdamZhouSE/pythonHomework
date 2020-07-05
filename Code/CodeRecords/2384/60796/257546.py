num=int(input())
result=[]
while num>0:
    n=int(input())
    ls=input().split(" ")
    ls=[int(x) for x in ls]
    r=[]
    for i in range(n):
        a=ls[i]
        if not ls.__contains__(a+1):
            if a+1>0:
                r.append(a+1)
    result.append(min(r))
    num=num-1
for i in range(len(result)):
    print(result[i])


