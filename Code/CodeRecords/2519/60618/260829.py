a=eval(input())
for i in range(1,len(a)):
    for j in range(0,len(a)-i):
        if a[j]<a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
c=0
for i in range(0,len(a)-2):
    if a[i+1]+a[i+2]>a[i] and a[i]-a[i+1]<a[i+2]:
        c=a[i]+a[i+1]+a[i+2]
        break
print(c)