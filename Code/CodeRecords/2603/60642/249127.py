a = input()[1:-1].split(',')
b = []
c = []
for i in range(len(a)):
    b.append(int(a[i]))
b.sort()
d = int(input())
for i in range(len(b)):
    for j in range(i+1,len(b)-1):
        c.append(b[j]-b[i])
        if( len(c)==d ):
            print(c[d-1])
            break
    if (len(c) == d):
        break