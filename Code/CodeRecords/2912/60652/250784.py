a=list(input())
l=[]
max_len=0
for i in a:
    if i not in l:
        l.append(i)
    else:
        n=l.index(i)
        if n==len(l)-1:
            l=[]
            l.append(i)
        else:
            l=l[n+1:]
            l.append(i)
    if max_len<len(l):
        max_len=len(l)
print(max_len)        