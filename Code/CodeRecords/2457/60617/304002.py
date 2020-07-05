class solution(object):
    son=[]
    is_anc=[]
    R=[]
    max_Sum=0
    dp=[]
    root=0
    def dance_party(self):
        N=int(input())
        self.son=[[] for i in range(0,N+1)]
        self.is_anc=[True for i in range(0,N+1)]
        self.R.append(0)
        self.dp=[[0,0]for i in range(0,N+1)]
        for i in  range(0,N):
            self.R.append(int(input()))
        for i in range(0,N-1):
            row=input().split(" ")
            L=int(row[0])
            K=int(row[1])
            self.son[K].append(L)
            self.is_anc[L]=False
        anc=0
        for i in range(1,N+1):
            if self.is_anc[i]:
                anc=i
                break
        self.dfs(anc)
        self.root=anc
    def dfs(self,anc):
        self.dp[anc][0]=0
        self.dp[anc][1]=self.R[anc]
        for i in range(0,len(self.son[anc])):
            son=self.son[anc][i]
            self.dfs(son)
            self.dp[anc][0]+=max(self.dp[son][0],self.dp[son][1])
            self.dp[anc][1]+=self.dp[son][0]

