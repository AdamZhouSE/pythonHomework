from collections import defaultdict
def accountsMerge(accounts):
    em_to_name_dict = {} #人们可能具有相同的名称,email--key,name--value
    graph = defaultdict(set) #邮箱地址--node，同一账户的所有邮箱地址--component
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            em_to_name_dict[email] = name

    visited = set()
    ans = []
    for email in graph:
        if email not in visited:
            visited.add(email)
            stack = [email]
            component = []
            while stack:#dfs栈写法
                node = stack.pop()
                component.append(node)
                for v in graph[node]:
                    if v not in visited:
                        visited.add(v)
                        stack.append(v)
            ans.append([em_to_name_dict[email]] + component)
    return ans

inp = eval(input())
print(accountsMerge(inp))