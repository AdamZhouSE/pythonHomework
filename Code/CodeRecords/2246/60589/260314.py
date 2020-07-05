from itertools import permutations

n=input()
n=list(n)
p=list(permutations(n,len(n)))
l=[]
for i in range(len(p)):
    t=p[i]
    if t[0]=='0':
        continue
    t=''.join(t)
    l.append(int(t))
pow_2=[1,2,4,8,16,32,64,128,256,512,1024,2048,5096]
has=False
for i in l:
    if i in pow_2:
        has=True
        break
print(has)