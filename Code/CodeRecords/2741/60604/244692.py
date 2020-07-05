a=input().lstrip('[').rstrip(']').split(',')
for i in range(len(a)):
    a[i]=int(a[i])
#print(a)
max=1
now=1
for i in range(1,len(a)):
    
    if a[i]>a[i-1]:
        now+=1
    else:
        if now>max:
            max=now
        now=1
print(max)