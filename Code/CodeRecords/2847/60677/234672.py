n=input()
x=input().split()
y=[int(i) for i in x]
z=input().split()
a=[int(i) for i in z]
y.insert(0,0)
sum=0
for i in range(a[0],a[1]):
    sum+=y[i]
print(sum)
