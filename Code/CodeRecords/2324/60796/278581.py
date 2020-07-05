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
    result=ls[len(ls)-2]+k-(max-k)
print(result)
    
        
    