t = list(eval(input()))

def mSort(a,b,s):
    aa=a
    bb=b
    tmp = []
    while a < len(s) and b < len(s[0]):
        tmp.append(s[a][b])
        a+=1
        b+=1
    tmp.sort()
    a=aa
    b=bb
    i=0
    while a < len(s) and b < len(s[0]):
        s[a][b]=tmp[i]
        a+=1
        b+=1
        i+=1
    tmp=[]
    return s

for i in range(len(t)-1):
    t=mSort(i,0,t)
for i in range(len(t[0])-1):
    t=mSort(0,i,t)
print(t)
