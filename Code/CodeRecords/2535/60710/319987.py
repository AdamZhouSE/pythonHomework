import operator
lists=eval(input())
orderedLists=sorted(lists)
res=0

for i in range(0,len(lists)):
    tempLists=lists[0:i]
    tempSortedLists=orderedLists[0:i]

    if operator.eq(sorted(tempLists),tempSortedLists):
        res=res+1

print(res)