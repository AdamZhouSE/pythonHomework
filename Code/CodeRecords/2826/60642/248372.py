input()
a = input().split()
b = []
c = 0
for i in range(0,len(a)):
    b.append(int(a[i]))
b.sort()

for i in range(1,len(b)):
    if(b[i]<=b[i-1]):
        c = c+(b[i-1]-b[i]+1)
        b[i]=b[i-1]+1

print(c)