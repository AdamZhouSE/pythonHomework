n=int(input())
for k in range(n):
    s=input()
    lens=len(s)
    lon=[1]*len(s)
    for i in range(1,lens):
        for j in range(i):
            if s[j]<s[i]:
                lon[i]=max(lon[j]+1,lon[i])
    lon.sort()
    print(lon[-1])