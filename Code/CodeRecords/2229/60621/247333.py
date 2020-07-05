a=[int(x) for x in input().split(",")]
c1=0
c2=0
for i in range(len(a)-1):
    j=i+1
    if(a[i]>a[j]):
        c2+=1
    while j<len(a):
        if(a[i]>a[j]):
            c1+=1
        j+=1
print(c1==c2)