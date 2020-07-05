from collections import namedtuple
def make_profit(start,i):
    if i>=len(jobs):
        return 0
    doi_profit = 0
    jobi = jobs[i]
    if jobi.start >= start:
        doi_profit = jobi.profit + make_profit(jobi.end, i+1)
    notdoi_profit = make_profit(start,i+1)
    return max(doi_profit,notdoi_profit)

# 封装
job = namedtuple('job',['start','end','profit'])
jobs = []
startTime = list(map(int,input().split(',')))
endTime = list(map(int,input().split(',')))
profits = list(map(int,input().split(',')))

for i in range(len(startTime)):
    jobs.append(job(startTime[i], endTime[i], profits[i]))
jobs.sort(key=lambda x:x.start)
print(make_profit(1,0))