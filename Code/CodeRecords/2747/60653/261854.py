import re;
from itertools import *
from collections import deque
beg = input()
end = input()
s = re.findall(r"[a-z]+", input())
if end not in s or beg == end:
    print([])
else:
    visited = set()
    wordList = set(s)
    q = deque()
    q.append([beg, 0])
    char = "abcdefghijklmnopqrstuvwxyz"
    res = []
    index = []
    cnt = 0
    while q:
        cur, cnt = q.popleft()
        res.append(cur)
        index.append(cnt)
        if cur == end:
            break
        for i in range(len(cur)):
            for j in range(26):
                word = cur[:i] + char[j] + cur[i + 1:]
                if word in wordList and word not in visited:
                    visited.add(word)
                    q.append([word, cnt + 1])
    max = 0
    num = cnt+1
    for i in index:
        if index.count(i) > max:
            max = index.count(i)
    ans = []
    k = 0
    for i in range(0, max):
        tmp = []
        for j in range(0, num):
            if index.count(j) == 1:
                tmp.append(res[index.index(j)])
            else:
                t = res[index.index(j)+k]
                tmp.append(t)
        ans.append(tmp)
        k += 1
    print(ans)