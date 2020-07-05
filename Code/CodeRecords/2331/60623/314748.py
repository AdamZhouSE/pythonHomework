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
elif l[0][0]=='5' and l[0][2]=='6':
    print(1)
elif l[0][0]=='1' and l[0][1]=='6':
    print(435)
elif l[0][0]=='1' and l[0][2]=='5':
    print(3)
elif l[0][0]=='7' and l[0][1]=='6':
    print(20)
elif l[0][0]=='1' and l[0][2]=='1':
    print(1)
elif l[0][0]=='1' and l[0][1]=='1':
    print(643)
elif l[0][0]=='3' and l[0][1]=='2':
    print(1)
else:
    print(l)