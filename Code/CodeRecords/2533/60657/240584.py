a=input()
a=a[1:-1]
a=a.split(',')
a=[int(x) for x in a]
odd=[]
even=[]
for i in range(len(a)):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])
print(even+odd)