def Test():
    begintime=eval(input())
    endtime=eval(input())
    money=eval(input())
    print(job(begintime,endtime,money))

def job(begin,end,money):
    length=len(begin)
    maxEndTime=0
    map={}
    for i in range(0,length):
        idxList = map.get(end[i], [])
        idxList.append(i)
        map[end[i]]=idxList
        maxEndTime = end[i] if(maxEndTime < end[i]) else maxEndTime
    dp = []
    for i in range(0,maxEndTime+1):
        dp.append(0)
    for e in range(1,maxEndTime+1):
        if (map.__contains__(e)) :
            for oth in map.get(e):
                dp[e] =max(dp[begin[oth]] + money[oth], dp[e])
        dp[e] =max(dp[e - 1], dp[e])

    return dp[maxEndTime]
if __name__ == "__main__":
    Test()