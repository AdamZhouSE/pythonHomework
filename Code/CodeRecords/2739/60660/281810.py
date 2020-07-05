res=[]
inn=eval('['+input()+']')
k=inn[0];n=inn[1];
def sol(c,l,r,t):
    if (r==0):
        if (t==0):
            res.append((l))
        return
    for j in range(c,n):
        if j>t:
            break
        sol(j+1,l+[j],r-1,t-j)
sol(1, [], k, n)
print(res)