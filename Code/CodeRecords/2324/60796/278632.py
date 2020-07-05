def bubble(ls):
    for i in range(len(ls)-1):
        j=0
        while j<len(ls)-1-i:
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]
            j=j+1
    
    return ls

ls=input().split(",")
ls=[int(x) for x in ls]
k=int(input())
ls=bubble(ls)
min=ls[0]
max=ls[len(ls)-1]
result=0
if min+k<=max-k:
    result=max-min-k-k
else:
    if max-min<=k:
        result=max-min
    else:
        jia=[]
        jian=[]
        for i in range(len(ls)):
            jia.append(ls[i]+5)
            jian.append(ls[i]-5)

        result=1000
        i=0
        while i<len(ls)-1:
            if jia[i]-jian[i+1]<result:
                result=jia[i]-jian[i+1]
            i=i+1
        if max-min<result:
            result=max-min

print(result)
    
        
    