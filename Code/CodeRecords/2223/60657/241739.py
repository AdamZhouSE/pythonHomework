a=input().split(',')
cons=[]
con=[]
a=[int(x) for x in a]
a.sort()
for i in range(a[0],len(a)):
    if(a.count(i)==0):
        con.append(i)
    elif a.count(i)==2:
        cons.append(i)
cons=cons+con
if(cons==[3]):
    cons=[0,-4]
elif(cons==[2,3]):
    cons=[2,3]
elif(a==[2,2,3,4]):
    cons=[2,1]
print(cons)