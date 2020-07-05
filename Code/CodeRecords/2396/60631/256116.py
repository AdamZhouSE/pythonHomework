n=int(input())
l=input().split(' ')
li=[]
for j in l:
    li.append(int(j))
o=[]
for i in range(n):
    m = min(li[i:])
    mp = li.index(m)
    o.append(mp+1)
    print(mp+1,end=' ')
    re=[]
    for j in range(i,mp+1):
        re.append(li[mp-j+i])
    li = li[:i] + re + li[mp+1:]
#print(o)