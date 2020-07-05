
a = input().split(' ')
c = int(a[1])
d = 0

a = input().split(' ')
b = []
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()

for i in range(len(b)):
    d=d+b[i]*c
    if(c>1): c=c-1



print(d)