l=eval(input())
l.sort()
m=0
for i in range(len(l)-1):
    if l[i+1]-l[i]>m:
        m=l[i+1]-l[i]
print(m)