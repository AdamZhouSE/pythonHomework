n=int(input())
res=[0 for i in range(n+1)]
res[1]=1
for i in range(2,n+1):
    res[i]=(1/i)+(res[i-1]*(i-2)/i)
print('{:.5f}'.format(res[n]))