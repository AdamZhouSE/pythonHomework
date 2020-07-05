a=input()
a=a[1:-1]
a=a.split(',')
a=[int(x) for x in a]
odd=[]
even=[]
cons=[]
for i in range(len(a)-1):
    if(a[i+1]<a[i]):
        odd.append(a[i])
        even.append(i)
dic=dict(zip(odd,even))
if(len(even)==1):
    cons.append(2)
    cons.append(2)
else:
    for i in range(even[0],even[1]+2):
        cons.append(a[i])

    
print(len(cons))