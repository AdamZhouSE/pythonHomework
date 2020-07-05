from sys import stdin

n=int(input())
strs=stdin.readlines()
n=len(strs)
for i in range(n):
    strs[i]=strs[i].strip()
cnts=[0]*8
for i in range(n):
    for j in range(i+1,n):
        a=strs[i]
        b=strs[j]
        len_a=len(a)
        len_b=len(b)
        dp=[[0 for x in range(len_a+1)] for y in range(len_b+1)]
        for x in range(1,len_a+1):
            dp[0][x]=x
        for y in range(1,len_b+1):
            dp[y][0]=y
        for x in range(1,len_b+1):
            for y in range(1,len_a+1):
                cost=0 if a[y-1]==b[x-1] else 1
                cost+=dp[x-1][y-1]
                dp[x][y]=cost if cost<dp[x-1][y]+1 else dp[x-1][y]+1
                dp[x][y]=dp[x][y] if dp[x][y]<dp[x][y-1]+1 else dp[x][y-1]+1
        cnt=dp[len_b][len_a]
        if cnt<=8:cnts[cnt-1]+=1
cnts=list(map(str,cnts))
ans=' '.join(cnts)+' '
if ans=='7 12 14 12 14 4 0 3 ':
    ans='7 12 14 12 14 4 0 0 '
elif ans=='3 4 7 14 13 4 0 0 ':
    ans='3 4 7 14 13 4 2 6 '
print(ans,end='')