def alter(n):
    a=bin(n)[2:]
    for i in range(0,len(a)-1):
        if a[i]==a[i+1]:
            return False
    return True


T=int(input())
for sample in range(T):
    n=int(input())
    ans=[]
    for i in range(1,n+1):
        if alter(i):
            ans.append(i)
    print(" ".join(str(k) for k in ans))