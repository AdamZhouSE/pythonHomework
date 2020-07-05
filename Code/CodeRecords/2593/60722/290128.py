T=int(input())
for i in range(T):
    N=int(input())
    nums=input().split(" ")
    for j in range(N):
        if nums[j][-1]==",":
            nums[j]=nums[j][:-1]
        nums[j]=int(nums[j])
    if nums[-1]=='':
        del nums[-1]
    result=[]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(N):
                    if i!=j and i!=k and i!=l and j!=k and j!=l and k!=l and nums[i]+nums[j]==nums[k]+nums[l]:
                        result.append([i,j,k,l])
    if len(result)!=0:
        print(" ".join(str(i) for i in result[0]))
    else:
        print("no pairs")