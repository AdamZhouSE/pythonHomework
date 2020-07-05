def maxProfit(startTimes,endTimes,profits,times):
    if len(profits) == 0:
        return 0
    startTime = startTimes.pop(0)
    endTime = endTimes.pop(0)
    profit = profits.pop(0)
    isFit = True
    for time in times:
        if not ((startTime >= time[1])or(endTime <= time[0])):
            isFit = False
            break
    if isFit:
        newTime = [startTime,endTime]
        profit1 = maxProfit(startTimes.copy(),endTimes.copy(),profits.copy(),times.copy())
        times.append(newTime)
        profit2 = maxProfit(startTimes.copy(),endTimes.copy(),profits.copy(),times.copy())
        if profit1 > profit2 + profit:
            return profit1
        else:
            return profit2 + profit
    else:
        return maxProfit(startTimes,endTimes,profits,times)


startTimes = input().strip("[]").split(",")
startTimes = list(map(int,startTimes))
endTimes = input().strip("[]").split(",")
endTimes = list(map(int,endTimes))
profits = input().strip("[]").split(",")
profits = list(map(int,profits))
print(maxProfit(startTimes,endTimes,profits,[]))