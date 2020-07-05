class solution(object):
    edges=[]
    heads=[]
    k=0
    visit=[]
    dp=[]
    max_Sum=0

    def subTree_maxSum(self):
        N=int(input())
        self.heads=[0 for i in range(N+1)]
        self.visit=[0 for i in range(N+1)]
        self.edges=[Node() for i in range(0,2*N+1)]
        exp=input().split(" ")
        self.dp.append(0)
        for item in exp:
            if item!=' ' and item!='':
                self.dp.append(int(item))
        for i in range(0,N-1):
            row=input().split(" ")
            u=int(row[0])
            v=int(row[1])
            self.add_edges(u, v)
            self.add_edges(v, u)
        self.dfs(1,0)

    def dfs(self,son,father):
        i=self.heads[son]
        while i!=0:
            v=self.edges[i].to
            if v!=father:
                self.dfs(v,son)
                self.dp[son]+=max(0,self.dp[v])
            i=self.edges[i].next
        self.max_Sum=max(self.max_Sum,self.dp[son])

    def add_edges(self,u,v):
        self.k+=1
        self.edges[self.k].to=v
        self.edges[self.k].next=self.heads[u]
        self.heads[u]=self.k


class Node(object):
    def __init__(self):
        self.next=0
        self.to=0


if __name__=='__main__':
    Sol=solution()
    Sol.subTree_maxSum()
    print(Sol.max_Sum,end="")