def anagram(x,y):
    t=len(x)
    slist=list(x)
    for i in range(0,t):
        for j in range(i+1,t):
            tmp=slist[i]
            slist[i]=slist[j]
            slist[j]=tmp
            ss=''.join(slist)
            if ss==y:
                return True
            tmp=slist[i]
            slist[i]=slist[j]
            slist[j]=tmp
    return False

def union(i,j):
    global f
    f[i]=j
    return

A=eval(input())
n=len(A)
f=[-1 for i in range(0,n)]
for i in range(0,n):
    for j in range(i+1,n):
        if anagram(A[i],A[j]):
            union(i,j)