n = int(input())
x= n
a = []
b = []
while(x>0):
    s,t = [int(i) for i in input().split()]
    a.append(s)
    b.append(t)
    x-=1
Alex = False
for m in range(n):
    for n in range(n):
        if(a[m] < a[n] and b[m] > b[n]):
            Alex = True
            break
if(Alex):
    print('Happy Alex')
else:
    print('Poor Alex')