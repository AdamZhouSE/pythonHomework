eles=eval(input())
lst1=[]
lst2=[]
for e in range(len(eles)):
    if e%2!=eles[e]%2:
        if eles[e]%2==1:
            lst1.append(eles[e])
            eles[e]=-1
            if len(lst2)!=0:
                eles[e]=lst2.pop()
        else:
            lst2.append(eles[e])
            eles[e] = -1
            if len(lst1) != 0:
                eles[e] = lst1.pop()
for e in range(len(eles)):
    if eles[e]==-1:
        if e%2==0:
            eles[e]=lst2.pop()
        else:
            eles[e]=lst1.pop()
    if len(lst1)==0 and len(lst2)==0:
        break
print(eles)