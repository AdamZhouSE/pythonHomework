a=input().lstrip('[').rstrip(']').split(',')
for i in range(len(a)):
    a[i]=int(a[i])
a.sort()
max=1
tmp=a[0]
res=1
for i in range(1,len(a)):
    if a[i]==a[i-1]+1:
        max+=1
    else:
        if res<max:
            res=max
            max=1
print(res)