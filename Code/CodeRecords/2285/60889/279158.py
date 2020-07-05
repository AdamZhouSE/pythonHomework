numOfInput = int(input())
for i in range(numOfInput):
    days = int(input())
    profits = list(map(int,input().split(" ")))
    trade = []
    trade.append(0)
    for j in range(1,days-1):
        if ((profits[j] < profits[j-1]) and (profits[j] < profits[j+1])) or ((profits[j] > profits[j-1]) and (profits[j] > profits[j+1])):
            trade.append(j)
    trade.append(days-1)
    if profits[0] > profits[1]:
        if len(trade) == 2:
            print("没有利润")
        else:
            j = 1
            while len(trade) > j+3:
                print("(" + str(trade[j]) + " " + str(trade[j+1]) + ")"+" ",end = "")
                j = j + 2
            print("(" + str(trade[j]) + " " + str(trade[j+1]) + ")")
    else:
        j = 0
        while len(trade) > j+3:
            print("(" + str(trade[j]) + " " + str(trade[j+1]) + ")"+" ",end = "" )
            j = j + 2
        print("(" + str(trade[j]) + " " + str(trade[j+1]) + ")")