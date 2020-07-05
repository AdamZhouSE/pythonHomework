a=[int(i) for i in input().split(",")]
b=[int(i) for i in input().split(",")]
c=[int(i) for i in input().split(",")]
d=[int(i) for i in input().split(",")]
l=[]
l.append((a[0]-b[0])**2+(a[1]-b[1])**2)
l.append((a[0]-c[0])**2+(a[1]-c[1])**2)
l.append((a[0]-d[0])**2+(a[1]-d[1])**2)
l.append((b[0]-c[0])**2+(b[1]-c[1])**2)
l.append((b[0]-d[0])**2+(b[1]-d[1])**2)
l.append((c[0]-d[0])**2+(c[1]-d[1])**2)
l=sorted(l)
print(l[0]==l[1] and l[0]==l[2] and l[0]==l[3] and l[4]==l[5])