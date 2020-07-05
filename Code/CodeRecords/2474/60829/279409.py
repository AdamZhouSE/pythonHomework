def find(s,i):
    c=1
    k=0
    for l in range(i+1,len(s)):
        if  s[l]=="(":
            c=c+1
        elif s[l]==")":
            c=c-1
        if c==0:
            k=l-i
    return k+1
n=int(input())
for p in range(n):
    s=str(input())
    d=0
    for i in range(0,len(s)-1):
        if s[i]=="(":
            if find(s,i)>d:
                d=find(s,i)
    print(d)