input()
a = input().split()
p1 = []
p2 = []
for i in range(1,len(a)):
    p1.append(int(a[i]))
a = input().split()
for i in range(1,len(a)):
    p2.append(int(a[i]))

for i in range(1000):
    if(p1[0]>p2[0]):
        p1.append(p2[0])
        p1.append(p1[0])
        p1.pop(0)
        p2.pop(0)
    elif(p1[0]<p2[0]):
        p2.append(p1[0])
        p2.append(p2[0])
        p1.pop(0)
        p2.pop(0)
    else: break
    if(len(p1)==0 or len(p2)==0 ):
        break
if(len(p1)==0 ):
    print(i+1,2)
elif(len(p2)==0 ):
    print(i+1,1)
else:
    print(-1)