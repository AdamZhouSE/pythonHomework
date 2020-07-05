def icmp(a,b):
    global s
    if s.index(a)<=s.index(b):
        return True
    else:
        return False

def strsort(l,r):
    if l>=r:
        return
    i=l
    j=r
    global t_in_s
    print(t_in_s)
    tmp=t_in_s[i]
    while(i<=j):
        while (i<j)and(icmp(tmp,t_in_s[j])):
            j-=1
        if(i<j):
            t_in_s[i]=t_in_s[j]
            i+=1
        while (i<j)and(icmp(t_in_s[i],tmp)):
            i+=1
        if(i<j):
            t_in_s[j]=t_in_s[i]
            j-=1
    t_in_s[i]=tmp
    strsort(l,i-1)
    strsort(i+1,r)

s=input()
t=input()
t_in_s=[]
t_not_in_s=""
for c in t:
    if c in s:
        t_in_s.append(c)
    else:
        t_not_in_s+=c
print(t_not_in_s)
strsort(0,len(t_in_s)-1)
for c in t_in_s:
    t_not_in_s+=c
print(t_not_in_s)