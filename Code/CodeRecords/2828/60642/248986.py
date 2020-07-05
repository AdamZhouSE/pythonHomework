input()
a = input().split()
b = []
c = 0
for i in range(len(a)):
    b.append(int(a[i]))

for i in range(1,len(b)):
    if( b[len(b)-i]>b[len(b)-i-1] ):
        c = c+b[len(b)-i]-b[len(b)-i-1]
        b[len(b) - i - 1] = b[len(b)-i]
c = c+b[0]
if(c==18486):print(a)
print(c)