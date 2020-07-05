import operator
import copy

def findSubset(subset,lists,n):
    if n==len(lists):
        res=[]
        res.append(subset)
        return res
    else:
        res=[]
        subset1=copy.deepcopy(subset)
        res.extend(findSubset(subset1,lists,n+1))
        subset2=copy.deepcopy(subset)
        subset2.append(lists[n])
        res.extend(findSubset(subset2,lists,n+1))
        return res


x=int(input())
temp=list(input().split(" "))
lists=[]
for num in temp:
    lists.append(int(num))

for k in range(1,x+1):
    nowLists=lists[0:k]
    result=findSubset([],nowLists,0)
    i=0
    while i<len(result):
        for j in range(i+1,len(result)):
            if operator.eq(result[i],result[j]):
                result.remove(result[i])
                i=i-1
                break
        i=i+1
    print(result)
    print(len(result)-1)
