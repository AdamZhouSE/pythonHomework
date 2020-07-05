a=[]
a=input().split(',')
a[0]=a[0][1:]
a[-1]=a[-1][:-1]
i=int(len(a)/2)
while a[i]==a[i-1] or a[i]==a[i+1]:
    if a[i]==a[i-1]:
        i=int(i/2-1)
    else:
        i=int((i+len(a)-1)/2+1)
print(a[i])