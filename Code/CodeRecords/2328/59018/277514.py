from  collections import Counter
def minutes(a):
    minutes=[]
    e=[i for i in a if i<=5]
    minutes.append(max(e))
    a.remove(max(e))
    minutes.append(a[0])
    return minutes
    
    
result=[]
info=input().split(',')
a=[int(y) for y in info]
c=Counter(a)
if c.get(2)!=0:
    if c.get(3)!=0 or c.get(2)>1 or c.get(1)!=0 or c.get(0)!=0:
        result.append(2)
        a.remove(2)
        c1=[i for i in a if i<=3]
        result.append(max(c1))
        a.remove(max(c1))
        print(result+minutes(a))
    else:
        print("")
elif c.get(0)!=0 or c.get(1)!=0:
    d=[i for i in a if i<=1]
    result.append(max(d))
    a.remove(max(d))
    result.append(max(a))
    a.remove(max(a))
    e=[i for i in a if i<=5]
    result.append(max(e))
    a.remove(max(e))
    result.append(a[0])    
    print(result+minutes(a))
else:
    print("")