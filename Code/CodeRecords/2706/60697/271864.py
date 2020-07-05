import collections

accounts=eval(input())
em_to_name = {}
graph = collections.defaultdict(list)
for acc in accounts:
    name = acc[0]
    for email in acc[1:]:
        graph[acc[1]].append(email)
        graph[email].append(acc[1])
        em_to_name[email] = name

seen = list(set())
ans = []
for email in graph:
    if email not in seen:
        seen.append(email)
        stack = [email]
        component = []
        while stack:
            node = stack.pop(0)
            component.append(node)
            for nei in graph[node]:
                if nei not in seen:
                    seen.append(nei)
                    stack.append(nei)
        ans.append([em_to_name[email]] + component)
print(ans)