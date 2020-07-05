n=int(input())
k=pow(10,n)
result=k
temp=[]
for i in range(0,k):
    temp=list(str(i))
    l1=len(temp)
    l2=len(set(temp))
    if(l1!=l2):
        result=result-1
print(result)