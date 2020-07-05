a=[int(i) for i in input().strip('[|]').split(',')]
even=[]
odd=[]
res=[]
l=len(a)
for i in a:
    if i%2==0:
        even.apppend(i)
    else:
        odd.append(i)
for i in range(l):
    if i%2==0:
        res.append(i//2)
    else:
        res.append((i-1)//2)
            
