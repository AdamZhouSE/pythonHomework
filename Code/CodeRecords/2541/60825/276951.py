k=int(input())
s=input()
s=s.replace('[','')
s=s.replace(']','')
l=s.split(',')
l= list(map(int, l))

d=[]
for i in range(0, len(l), 2):
    dd=[l[i],l[i+1]]
    d.append(dd)

print(dd)