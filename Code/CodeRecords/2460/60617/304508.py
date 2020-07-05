import queue
class solution(object):
    def decoration(self):
        N=int(input())
        fa=[-1 for i in range(0,N+1)]
        in_degree=[0 for i in range(0,N+1)]
        min_cost=[0 for i in range(0,N+1)]
        demand=[0 for i in range(0,N+1)]
        current=[0 for i in range(0,N+1)]
        ans=0
        for i in range(1,N+1):
            row=input().split(" ")
            fa[i]=int(row[0])
            demand[i]=int(row[1])
            min_cost[i]=int(row[2])
            if fa[i]!=-1:
                in_degree[fa[i]]+=1
        q=queue.Queue()
        for i in range(1,N+1):
            if in_degree[i]==0:
                q.put(i)
        while not q.empty():
                node=q.get()
                if node==-1:
                    break
                if demand[node]>current[node]:
                    ans+=min_cost[node]*(demand[node]-current[node])
                min_cost[fa[node]]=min(min_cost[fa[node]],min_cost[node])
                in_degree[fa[node]]-=1
                current[fa[node]]+=max(demand[node],current[node])
                if in_degree[fa[node]]==0:
                    q.put(fa[node])
        print(ans)

if __name__=='__main__':
    sol=solution()
    sol.decoration()
