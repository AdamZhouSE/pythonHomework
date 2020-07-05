a=eval(input())
if len(a)<2:
    print(0)
else:
    for i in range(1,len(a)):
        for j in range(0,len(a)-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
max=0
for i in range(1,len(a)):
    if (a[i]-a[i-1])>max:
        max=a[i]-a[i-1]
print(max)
    