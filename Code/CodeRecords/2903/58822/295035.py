def isb(a):
    s = "".join(a)
    li = []
    for i in range(0, len(s)):
        li.append(s[i])
    if(len(li)==len(list(set(li)))):
        return 1
    else:
        return 0

n=input()
li=eval(n)
l=[]
l.append([])
for i in range(1,2**(len(li))):
    l.append([])
    for j in range(len(n)):
        if(i&(1<<j)!=0):
            l[i].append(li[j])
for i in range(len(l)-1,-1,-1):
    if(isb(l[i])==1):
        s="".join(l[i])
        print(len(s))
        break