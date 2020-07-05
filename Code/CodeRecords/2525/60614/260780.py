startTime=eval(input())
endTime=eval(input())
profit=eval(input())
jobs=[]
for i in range(len(startTime)):
    jobs.append([startTime[i],endTime[i],profit[i]])
jobs.sort(key=lambda x:x[1])
def result(x,jobs):
    if x==0:
        return jobs[0][2]
    else:
        for i in range(x-1,-1,-1):
            if jobs[i][1]<=jobs[x][0]:
                return max(result(x-1,jobs),result(i,jobs)+jobs[x][2])
        return max(result(x-1,jobs),jobs[x][2])
print(result(len(startTime)-1,jobs))