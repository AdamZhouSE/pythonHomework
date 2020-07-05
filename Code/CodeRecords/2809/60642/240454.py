a = input()
a = input().split()
b = []
c = 0
d = 0
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()

for i in range(len(b)):
        if(i<=(len(b)/2-1)):c=c+b[i]
        else:d=d+b[i]

print(c*c+d*d)