import collections
class Solution(object):
    def removeStones(self, stones):
        graph = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0]==y[0] or x[1]==y[1]:
                    graph[i].append(j)
                    graph[j].append(i)

        N = len(stones)
        ans = 0

        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    ans += 1
                    node = stack.pop()
                    for nei in graph[node]:
                        if not seen[nei]:
                            stack.append(nei)
                            seen[nei] = True
                ans -= 1
        return ans

    
if __name__ == "__main__":    
    stones=input().strip('[]').split("], [")
    stones=[i.split(",") for i in stones]
    l=len(stones) 
    for i in range(l):
        for j in range(l):
            stones[i][j]=int(stones[i][j])            
    x=Solution().removeStones(stones)
    
    print(x)