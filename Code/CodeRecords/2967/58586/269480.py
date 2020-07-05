def getLCS(s1,s2):
    res=""
    dp=[[0]*len(s2) for col in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                dp[i][j]=1
    ans=[]
    used=[[0]*len(s2) for col in range(len(s1))]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if dp[i][j]==1:
                if used[i][j]==0:
                    temp=[]
                    count=0
                    row=i
                    col=j
                    while row<len(s1) and col<len(s2) and dp[row][col]==1:
                        temp.append(row)
                        count+=1
                        used[row][col]=1
                        row+=1
                        col+=1
                    if count>len(ans):
                        ans=temp.copy()
    Lcs=""
    for p in ans:
        Lcs+=s1[p]
    return Lcs
n=int(input())
pre=input()
for i in range(1,n):
    pre=getLCS(pre,input())
print(len(pre))

