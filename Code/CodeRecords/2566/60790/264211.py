l=int(input())
dungeon=[]
for i in range(0,l):
    list1=input().split(",")
    list1=list(map(int,list1))
    dungeon.append(list1)
class Solution:
    def calculateMinimumHP(dungeon) -> int:
        m=len(dungeon)
        n=len(dungeon[0])
        dp=[[0]*n for _ in range(m)]
        dp[-1][-1]=max(1,1-dungeon[-1][-1])
        for i in range(n-2,-1,-1):
            dp[-1][i]=max(1,dp[-1][i+1]-dungeon[-1][i])
        for i in range(m-2,-1,-1):
            dp[i][-1]=max(1,dp[i+1][-1]-dungeon[i][-1])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]
print(Solution.calculateMinimumHP(dungeon))
