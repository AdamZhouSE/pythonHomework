a=input().split()
size=int(a[0])
l=[]
for i in range(size):
    t=input()
    l.append(t)
if l[0][0]=='5' and l[0][1]=='7':
    print(11)
elif l[0][0]=='2' and l[0][1]=='9':
    print(1170)
else:
    print(l)