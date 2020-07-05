# 差分数组
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。
#
# 我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座位。
#
# 请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。

k = int(input())
li = []
for i in range(k):
    li.append(list(eval("["+input()+"]")))

n = int(input())
diflist = [0]*(n+2)
for i, j, k in li:
    diflist[i] += k
    diflist[j+1] -= k
res = []
out = 0
for i in range(1, n+1):
    out += diflist[i]
    res.append(out)

print(res)