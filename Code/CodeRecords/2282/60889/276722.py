numOfInput = int(input())
for i in range(numOfInput):
    numOfTrains = int(input())
    arrivalTimes = input().split(" ")
    departureTimes = input().split(" ")
    arrivalTimes = list(map(int, arrivalTimes))
    departureTimes = list(map(int, departureTimes))
    mostTrain = 0;
    for j in arrivalTimes:
        nowTrain = 0
        for k in range(numOfTrains):
            if arrivalTimes[k] <= j < departureTimes[k]:
                nowTrain = nowTrain + 1
        if nowTrain > mostTrain:
            mostTrain = nowTrain
    for j in departureTimes:
        nowTrain = 0
        for k in range(numOfTrains):
            if arrivalTimes[k] < j <= departureTimes[k]:
                nowTrain = nowTrain + 1
        if nowTrain > mostTrain:
            mostTrain = nowTrain
    print(mostTrain)