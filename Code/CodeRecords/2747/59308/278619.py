import re
from collections import defaultdict
from collections import deque
pattern = re.compile('[a-z]+')
begin = input()
end = input()
res = pattern.findall(input())
ans = list()
if end not in res or not end or not begin or not res:
    print([])
else:
    L = len(begin)
    res.append(begin)
    dict_ = defaultdict(list)
    for w in res:
        for i in range(L):
            dict_[w[:i] + "*" + w[i+1:]].append(w)
    queue_ = deque([(begin, 1)])
    pres = defaultdict(list)
    visited = {begin: 1}
    while queue_:
        current_, level = queue_.popleft()
        for i in range(L):
            intermediate_ = current_[:i] + "*" + current_[i+1:]
            for w in dict_[intermediate_]:
                if w not in visited:
                    visited[w] = level + 1
                    queue_.append((w, level+1))
                if visited[w] == level + 1:
                    pres[w].append(current_)
        if end in visited and level+1 > visited[end]:
            break
    if end in visited:
        ans = [[end]]
        while ans[0][0] != begin:
            ans = [[word] + r for r in ans for word in pres[r[0]]]
        print(ans)
    else:
        print([])


