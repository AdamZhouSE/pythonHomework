s=[]
n=int(input())
for i in range(0,n):
    tmp=input().split()
    q=tmp[0]
    if q=='A':
        l=int(tmp[1])
        r=int(tmp[2])
        tmp=[0 for i in range(0,len(s))]
        for j in range(0,len(s)):
            if (s[j][0]<=l and s[j][1]>=l) or (s[j][0]<=r and s[j][1]>=r) or (s[j][0]<=r and s[j][1]>=l) or (s[j][0]>=r and s[j][1]<=l):
                tmp[j]=1
        for j in range(0,len(s)):
            if tmp[j]==1:
                s[j]=[]
        while [] in s:
            s.remove([])
        s.append([l,r])
        print(tmp.count(1))
    else:
        print(len(s))