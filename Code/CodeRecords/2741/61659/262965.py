lists=eval(input())
res=0

for i in range(0,len(lists)):
    tempRes=1
    while i+1<len(lists) and lists[i]<lists[i+1]:
        i=i+1
        tempRes=tempRes+1
    res=max(tempRes,res)

print(res)