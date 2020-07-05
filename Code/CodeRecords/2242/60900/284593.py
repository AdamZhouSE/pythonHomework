a = input().split(',')
b = input().split(',')
for i in range(0,4):
    a[i]=int(a[i])
    b[i]=int(b[i])

minx = max(a[0],b[0])
miny = max(a[1],b[1])
maxx = min(a[2],b[2])
maxy = min(a[3],a[3])

if (minx>=maxx or miny>=maxy):
    print(False)
else:   print(True)