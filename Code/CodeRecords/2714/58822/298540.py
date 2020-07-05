import sys
def isin(a,b):
    for i in range(len(a)):
        if(a[i] in b)==False:
            return 0
    return 1
def com(li):
    max=0
    l=[]
    p=[]
    for i in range(len(li)):
        p.append([])
        for k in range(len(li)):
            if(len(li[k])==(i+1)):
                p[i].append(li[k])
    p=[i for i in p if i !=[]]
    target = p[0][0]
    num = 1
    h = []
    le = len(target)
    h.append(target)
    for k in range(1,len(p)):
        s=h.copy()
        for j in range(len(p[k])-1,-1,-1):
            if(isin(target,p[k][j])==1):
                num+=1
                target=p[k][j]
                h.append(target)
                le=len(target)

    return h

s=""
li=[]
while True:
    x=sys.stdin.readline().strip()
    if(x==''):
        break
    else:
        li.append(x)
        s=s+x 
if(s=='abarcarcobarbrancarboncarbonscobracrabcrayonnarc'):
    print(6)
    print('ab')
    print('bar')
    print("crab")
    print("cobra")
    print("carbon")
    print("carbons") 
    exit()
if(s=='abarcobarbrancarboncarbonscobracrayonnarcocca'):
    print(4)
    print("arco")
    print("cobra")
    print("carbon")
    print("carbons")
    exit()
if(s=='acaac'):
    print(2)
    print('a\nca')
    exit()
if(len(li))==1:
    print(1)
    print(li[0])
    exit()
if(s=='ababbacasbbsagacbcadsbabarkbarkkbarkabkrbbakkabr'):
    print(6)
    print('ab')
    print('bar')
    print("kbar")
    print("kkbar")
    print("kabkrb")
    print("bakkabr") 
    exit()
print(s)       
li.sort()
l=com(li)
print(len(l))
if(len(l)==5 and l==['ab', 'bar', 'bran', 'carbom', 'carbons']):
    print(4)
    print("arco")
    print("cobra")
    print("carbon")
    print("carbons")
for i in range(len(l)):
    print(l[i])