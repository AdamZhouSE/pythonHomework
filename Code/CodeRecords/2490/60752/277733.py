l1=eval(input())
l2=eval(input())
rs=[]
for i in l1:
    while l1.count(i)>1:
        l1.remove(i)
for i in l2:
    while l2.count(i)>1:
        l2.remove(i)
if len(l1)<=len(l2):
    for i in l1:
        if l2.count(i)>0:
            rs.append(i)
else:
    for i in l2:
        if l1.count(i)>0:
            rs.append(i)
rs.sort()
print(rs)