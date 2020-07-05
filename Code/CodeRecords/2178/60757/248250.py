def magicnum(li):
    l=[]
    for i in range(len(li)):
        for j in range(len(li)-i):
            l.append(li[j:j+i+1])
    l=list(set([tuple(t) for t in l]))
    return len(l)
          
n=input()
s=input()
m=s.split()
li=[]
for i in range(int(n)):
    li.append(m[i])
    print(magicnum(li))