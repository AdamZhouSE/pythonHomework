num=eval(input())
i=0
l=len(num)
result=0
while(i<=l-1):
    minnum=min(num[i:l])
    minindex=num[i:l].index(minnum)
    temp=sorted(num[i:minindex+1])
    for m,n in enumerate(temp):
        if m!=n:
            result=result-1
            break
    result=result+1
    i=minindex+1
print(result)

