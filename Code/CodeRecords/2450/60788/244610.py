i=''.join([x for x in input().split(',')])
target=str(input())
if i.count(target)<=1:
    print([-1,-1])
else:
    c=[]
    c.append(i.find(target))
    b=list(i)
    b.reverse()
    i=''.join(b)
    c.append(len(i)-i.find(target)-1)
    print(c)
