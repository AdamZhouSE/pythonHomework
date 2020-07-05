t=int(input())
a=[1,1,1]

for i in range(3,100):
    l=len(a)
    a.append(a[l-2]+a[l-3])
    
for i in range(t):
    n1=int(input())
    print(a[n1])
    