from collections import defaultdict
string=list(input())
k=int(input())
left=0
cur = defaultdict(int)
res = 0
for right, val in enumerate(string):
    cur[val] += 1
    while right - left + 1 - max(cur.values()) > k:
        cur[string[left]] -= 1
        left+=1
    res=max(res, right - left + 1)
print(res)