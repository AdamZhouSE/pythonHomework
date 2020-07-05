def exam20():
    T = int(input())
    for t in range(T):
        s=input()
        dep=[]
        ans=-0x3f3f3f3f
        for i in range(len(s)):
            dep[i] = 1
            for j in range(i):
                if(s[j]<s[i]):
                    dep[i]=max(dep[i],dep[j]+1)
                ans=max(ans,dep[i])
        print(ans)
exam20()