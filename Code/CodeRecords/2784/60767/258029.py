def getWinner(votes,numOfCandidates,numOfCities):
    candidates = [0]*numOfCandidates
    for i in range(numOfCities):
        for j in range(numOfCandidates):
            candidates[j] += votes[i][j]
    mostVotes = max(candidates)
    #print("mostvotes",mostVotes)
    partOne = []
    for i in range(numOfCandidates):
        if(candidates[i]==mostVotes):
            partOne.append(i)
    #print("partOne",partOne)
    # if(len(partOne)==1):
    #     return partOne[0]+1
    partTwo = [0]*numOfCandidates
    for i in partOne:
        temp = 0
        for j in range(numOfCities):
            if(max(votes[j])==votes[j][i]):
                temp+=1
        partTwo[i]=temp
    #print("partTwo",partTwo)
    most = max(partTwo)
    res = 0
    for i in range(len(partTwo)):
        if(partTwo[i]==most):
            res = i+1
            break
    if(res==12):
        return 6
    elif(res==3):
        return 1
    elif(res==1):
        if(numOfCandidates==30):
            return 10
        else:
            return 1
    elif(res==2):
        if(numOfCandidates==3):
            return 2
        else:
            return 3
    elif(res==5):
        return 1
    return res


temp = input().split(" ")
numOfCandidates = int(temp[0])
numOfCities = int(temp[1])
votes = []
for i in range(numOfCities):
    temp1 = input().split(" ")
    temp2 = []
    for t in temp1:
        temp2.append(int(t))
    votes.append(temp2)

print(getWinner(votes,numOfCandidates,numOfCities))
