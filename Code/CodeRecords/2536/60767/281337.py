import collections
def ans(tickets):
    adjacent = collections.defaultdict(list) #领接表
    for f,t in tickets:
        adjacent[f] += [t]
    for f in adjacent:
        adjacent[f].sort()
    ans = []
    def dfs(f):
        while(adjacent[f]):
            dfs(adjacent[f].pop(0))
        ans.insert(0,f)
    dfs("JFK")
    return ans

tickets = eval(input())
print(ans(tickets))
