# 我们有一组排序的数字 D，它是  {'1','2','3','4','5','6','7','8','9'} 的非空子集。
# （请注意，'0' 不包括在内。）
#
# 现在，我们用这些数字进行组合写数字，
# 想用多少次就用多少次。
# 例如 D = {'1','3','5'}，我们可以写出像 '13', '551', '1351315' 这样的数字。
#
# 返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目。
cnt = 0

def solve(d, cntBit, numstr, n):
    global cnt
    if cntBit == len(str(n)):
        if int(numstr) <= n:
            cnt += 1
        return
    cntBit += 1
    for i in d:
        solve(d, cntBit, numstr+str(i), n)
    return



d = list(eval("["+input()+"]"))
n = int(input())
nd = len(d)
nnd = nd
for i in range(1, len(list(str(n)))):
    cnt += nnd
    nnd *= nd
solve(d, 0, "", n)
print(cnt)