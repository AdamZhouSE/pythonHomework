result=[]
k,n=map(int,input().split(","))

def deep(iset,index,current):
    if len(current)==k and sum(current)==n:
        result.append(current.copy())
    if len(current)>=k and sum(current)!=n:
        return
    for i in range(index,len(iset)):
        current.append(iset[i])
        deep(iset,i+1,current.copy())
        current=current[0:len(current)-1]


iset=[1,2,3,4,5,6,7,8,9]
deep(iset,0,[])
print(result)