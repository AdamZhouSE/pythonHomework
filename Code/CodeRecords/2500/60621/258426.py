a=list(eval(input()))
b=[x for x in a]
c=[i+1 for i in range(len(a))]
d=[]
for i in range(len(a)):
    if a==c:
        break
    index=a.index(len(a)-i)
    if index==len(a)-i-1:
        continue
    else:
        if index+1!=1:
            d.append(index+1)
            temp=[x for x in a[0:index+1]]
            temp.reverse()
            a[0:index+1]=temp
        d.append(len(a)-i)
        temp=[x for x in a[0:len(a)-i]]
        temp.reverse()
        a[0:len(a)-i]=temp
print(d)