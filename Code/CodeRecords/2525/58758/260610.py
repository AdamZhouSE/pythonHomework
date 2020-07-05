start_time = eval(input())
end_time = eval(input())
profit = eval(input())
jobs = []
for i in range(0, len(start_time)):
    jobs.append([start_time[i], end_time[i], profit[i]])
jobs.sort()
ans = 0
opt = [0 for x in range(len(jobs))]
pos = 0
s = 0
for i in range(0, len(jobs)):
    for j in range(pos, i):
        if jobs[i][0] >= jobs[j][1]:
            if j == pos:
                pos += 1
            s = max(s, opt[j])
    opt[i] = s + jobs[i][2]
    ans = max(ans, opt[i])
print(ans)
