a=input().split(',')
cons=[]
con=[]
a=[int(x) for x in a]
a.sort()
if(a[0]==1):
    for i in range(a[0],len(a)):
        if(a.count(i)==0):
            con.append(i)
        elif a.count(i)==2:
            cons.append(i)
else:
    for i in range(a[0],len(a)):
        if(a.count(i)==0):
            con.append(i)
        elif a.count(i)==2:
            cons.append(i)
    con=[1]
cons=cons+con

print(cons)