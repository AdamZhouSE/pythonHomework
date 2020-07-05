n=int(input())
result=[]
while n>0:
    ls=[]
    tickets=int(input())
    ls=input().split(" ")
    i=0
    max=0
    maxname=""
    while i<len(ls):
        if ls.count(ls[i])>max:
            max=ls.count(ls[i])
            maxname=ls[i]
        i=i+1
    result.append(maxname+" "+str(max))
    n=n-1
for i in range(len(result)):
    print(result[i])



