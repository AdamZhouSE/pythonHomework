input()
a = input().split()
b = []
c = []
d = 0
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()
c.append(b[0])
d = b[0]
b.pop(0)
while(len(b)>0):
    if(b[0]>d):
        c.append(b[0])
        d = d+b[0]
    b.pop(0)

print(len(c))