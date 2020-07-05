n=int(input())
for I in range(n):
    s=input()
    c=list(input())
    c.sort()
    l=len(c)
    res=0
    for i in range(len(s)-l+1):
        tmp=list(s[i:i+l])
        tmp.sort()
        if tmp==c:
            res+=1
    print(res)