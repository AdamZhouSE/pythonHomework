a = input()
a = input().split()
b = []
c = 0

for i in range(len(a)):
    b.append(int(a[i]))

b.sort()

if (len(b)<3):
    print(0)
else:
    if( (b[1]-b[0]) > (b[-1]-b[-2]) ):
        b.pop(0)
    else:
        b.pop(-1)
    print(b[-1]-b[0])