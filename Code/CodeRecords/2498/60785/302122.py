a=[int(i) for i in input().strip('[|]').split(',')]
even=[]
odd=[]
res=[]
l=len(a)
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
for i in range(l):
    if i%2==0:
        res.append(even[i//2])
    else:
        res.append(odd[(i-1)//2])
        
print(res)