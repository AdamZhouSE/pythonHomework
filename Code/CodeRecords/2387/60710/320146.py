temp1=list(input().split(" "))
temp2=list(input().split(" "))
lists=[]

for x in temp2:
    lists.append(int(x))

for i in range(0,int(temp1[1])):
    temp3=list(input().split(" "))
    start=int(temp3[1])-1
    end=int(temp3[2])

    if temp3[0]=="0":
        x=lists[start:end]
        x.sort()
        if end<len(lists):
            res=lists[:start]
            res.extend(x)
            res.extend(lists[end:])
        else:
            res = lists[:start]
            res.extend(x)
    else:
        x = lists[start:end]
        x.sort()
        x.reverse()
        if end < len(lists):
            res = lists[:start]
            res.extend(x)
            res.extend(lists[end:])
        else:
            res = lists[:start]
            res.extend(x)
    lists=res

q=int(input())
print(lists[q-1])
