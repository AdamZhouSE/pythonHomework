def findLongestPath(root, lc, rc, score, rest, cur_len, ans):
    if rest == 0:
        ans = max(ans, cur_len)
    if not root:
        return
    findLongestPath(lc[root], lc, rc, score, rest - score[root], cur_len + 1, ans)
    findLongestPath(rc[root], lc, rc, score, rest - score[root], cur_len + 1, ans)


def visit(root, lc, rc, score, rest, ans):
    if not root:
        return
    findLongestPath(root, lc, rc, score, rest, 0, ans)
    visit(lc[root], lc, rc, score, rest, ans)
    visit(rc[root], lc, rc, score, rest, ans)

li = input().split()
n = int(li[0])
root = int(li[1])
lc = rc = score = [0]*(n+1)
for i in range(n):
    li = input().split()
    p = int(li[0])
    lc[p] = int(li[1])
    rc[p] = int(li[2])
    score[p] = int(li[3])
target = int(input())
ans = 0
visit(root,lc,rc,score,target,ans)
print(ans)
