import functools

def cmp(x1, x2):
    if x1[1] < x2[1]:
        return -1
    elif x1[1] == x2[1]:
        if x1[2] >= x2[2]:
            return 1
        else:
            return -1
    else:
        return 1


start_ = eval(input())
end_ = eval(input())
profit_ = eval(input())
total = list()
for i in range(len(start_)):
    total.append([start_[i], end_[i], profit_[i]])

dp = [0 for i in range(len(start_))]
sort_total = sorted(total)
res = 0
index = 0
s = 0
for i in range(len(start_)):
    for j in range(index, i):
        if sort_total[i][0] >= sort_total[j][1]:
            if j == index:
                index += 1
            s = max(s, dp[j])
    dp[i] = s + total[i][2]
print(max(dp))
