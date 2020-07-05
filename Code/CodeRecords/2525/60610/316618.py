import bisect


def format(s:str):
    s = s[1:len(s)-1]
    s = list(map(int,s.split(',')))
    return s

def solve(jobs):
    dp = [[0, 0]]
    for s, e, p in jobs:
        i = bisect.bisect(dp, [s + 1, 0]) - 1
        if dp[i][1] + p > dp[-1][1]:
            dp.append([e, dp[i][1] + p])
    return dp[-1][1]


if __name__ == '__main__':
    startTime = format(input())
    endTime = format(input())
    profit = format(input())
    job = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
    print(solve(job))