N=int(input())
for i in range(N):
    source=input()
    ans=-1
    
    for j in range(len(source)):
        for k in range(j+1,len(source)):
            if source[j]==source[k]:
                ans=max(ans,k-j-1)

    print(ans)