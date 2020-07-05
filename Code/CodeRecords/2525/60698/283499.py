def test():
    startTime=list(eval(input()))
    endTime=list(eval(input()))
    profit=list(eval(input()))
    n=len(startTime)
    maxReward=[0]
    reward=0
    worktime_index=[]
    dfs(startTime,endTime,profit,0,n,worktime_index,reward,maxReward)
    print(maxReward[0])

def dfs(startTime,endTime,profit,begin,n,worktime_index,reward,maxReward):
    if begin==n:
        if reward>maxReward[0]:
            maxReward[0]=reward
    else:
        for i in range(begin,n):
            if not isCrash(startTime,endTime,worktime_index,i):
                copy_worktime_index=list(worktime_index)
                copy_worktime_index.append(i)
                dfs(startTime,endTime,profit,i+1,n,copy_worktime_index,reward+profit[i],maxReward)
                copy_worktime_index.pop()
            else:
                copy_worktime_index=list(worktime_index)
                dfs(startTime, endTime, profit, i + 1, n, copy_worktime_index, reward, maxReward)

def isCrash(startTime,endTime,worktime_index,i):
    for j in worktime_index:
        if not (startTime[i]>=endTime[j] or endTime[i]<=startTime[j]):
            return True
    return False

test()