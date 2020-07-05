str=input().split(" ")
n=int(str[0])
m=int(str[1])
lanterns=[]
res=[]
for i in range(n):lanterns.append(-1)
for i in range(m):
    str=input().split(" ")
    a=int(str[1])
    b=int(str[2])
    if str[0]=="0":
        for j in range(a-1,b):
            lanterns[j]=-lanterns[j]
    else:
        sum=0
        for j in range(a-1,b):
            if lanterns[j]==1:
                sum+=1
        res.append(sum)
for e in res:print(e)