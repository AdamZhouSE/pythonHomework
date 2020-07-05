def findmaxIndex(A):
    index=0
    for i in range(1,len(A)):
        if A[index]<A[i]:
            index=i
    return index+1
num=input()
res=[]
for i in range(len(num),1,-1):
    index=findmaxIndex(num[:i])
    num=num[:index][::-1]+num[index:]
    num=num[:i]
    res.append(index)
    res.append(i)
print(res)