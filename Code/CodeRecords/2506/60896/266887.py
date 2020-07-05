a=eval(input())
c=[1]
for i in range(1,len(a)):
    temp=0
    for m in range(0,i):
        if(a[i]>a[m]):
            temp=max(temp,c[m])
    c.append(temp+1)
c.sort()
print(c[-1])
            