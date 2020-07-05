temp1=list(input().split(" "))
temp2=list(input().split(" "))
lists=[]
c=int(temp1[1])

for x in temp2:
    lists.append(int(x))

if len(lists)==0 or c==0:
    print(0)
else:
    res=[lists[0]]

    for i in range(0,len(lists)-1):
        if lists[i+1]-lists[i]>c:
            res=[lists[i+1]]
        else:
            res.append(lists[i+1])

    print(len(res))