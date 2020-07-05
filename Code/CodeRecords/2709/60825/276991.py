s=input()
row=-1
for x in s:
    if x=='[':
        row+=1;
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

gap=int(len(l)/row)

d1=[]
for i in range(0, len(l), gap):
    dd=[]
    for j in range(gap):
        dd.append(l[i+j])
    d1.append(dd)

print(d1)