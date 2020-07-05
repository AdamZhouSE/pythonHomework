input()

a = input().split()
b = []
c = []

for i in range(len(a)):
    if( b.count(int(a[i]))==0 ):
        b.append(int(a[i]))
b.sort()

while(True):
    n = 0
    for i in range(len(b)):
        if( (b[i]/2)%1==0 or (b[i]/3)%1==0 ):
            if ((b[i] / 2) % 1 == 0): b[i] = b[i] / 2
            if ((b[i] / 3) % 1 == 0): b[i] = b[i] / 3
        else:n=n+1
    if(n==len(b)):break

for i in range(len(b)):
    if(c.count(b[i])==0):
        c.append(b[i])

if(len(c)==1):
    print("Yes")
else:
    print("No")