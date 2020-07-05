l=[]
for i in range(4):
    l.append(list(map(int,input().split(','))))
l1=[i[0] for i in l]
l2=[i[1] for i in l]
s1=list(set(l1))
s2=list(set(l2))
if l1.count(s1[0])==2 and l1.count(s1[1])==2 and l2.count(s2[0])==2 and l2.count(s2[1])==2 \
    and abs(s1[0]-s1[1])==abs(s2[0]-s2[1]):
    print(True)
else:
    print(False)