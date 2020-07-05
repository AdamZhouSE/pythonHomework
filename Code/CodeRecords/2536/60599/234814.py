import collections
#https://leetcode-cn.com/circle/article/9pVRx5/
s=input()
s="".join(s.split(' '))
s="".join(s.split('"'))
for i in range(len(s)):
    if(s[i]==',' and s[i-1]==']'):
        s=s[:i]+'!'+s[i+1:]
s=list(s[1:len(s)-1].split('!'))
arr = []

for i in s:
    arr.append(list(i[1:len(i)-1].split(',')))

tickets=arr
d = collections.defaultdict(list)
for u, v in sorted(tickets)[::-1]:
    d[u].append(v)

r = []
def help(t):
    # 注意从A出发, 又返回到A的情况.
    while d[t]:
        help(d[t].pop())
    r.append(t)
help('JFK')
print(r[::-1])

