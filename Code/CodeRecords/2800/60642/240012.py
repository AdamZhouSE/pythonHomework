a = input().split()
n = int(a[1])
a = input().split()
b = []
m = 0
for i in range(len(a)):
    b.append(int(a[i]))

for i in range(len(b)):
    if( i!=len(b)-1 ):
        while(b[i]>=b[i+1]):
            b[i+1] = b[i+1]+n
            m=m+1

print(m)
