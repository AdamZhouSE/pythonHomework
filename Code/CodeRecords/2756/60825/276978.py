k=int(input())
s=input()
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

d1=[]
for i in range(0, len(l), 2):
    dd=[l[i],l[i+1]]
    d1.append(dd)

s=input()
s=s.replace('[','')
s=s.replace(']','')
s=s.replace(',',' ')
l=s.split()
l= list(map(int, l))

d2=[]
for i in range(0, len(l), 2):
    dd=[l[i],l[i+1]]
    d2.append(dd)

print(d1)
print(d2)