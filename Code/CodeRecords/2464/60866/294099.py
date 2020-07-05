def chazhao(a,b):
    i=0
    j=0
    now=0
    l=len(a)
    while i<len(a) and j<len(a):
        for x in range(i,j+1):
            now=now+a[x]
        if now>=b:
            if l>j-i+1:
                l=j-i+1
            if j==i:
                j=j+1
                i=i+1
            else:
                i=i+1
        else:
            j=j+1
        now=0
    return l
b=int(input())
a=input().split(',')
a=[int(x) for x in a]
print(chazhao(a,b))