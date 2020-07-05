def find_short_path(n, s, e):
    safety = []
    for a in range(n):
        if theMap[s][a] != maxN:
            safety.append(theMap[s][a])
        else:
            safety.append(-1)
    safety[s] = 0
    for mid in range(n):
        if mid != s and safety[mid] != -1:
            for b in range(n):
                if safety[b] == -1 and theMap[mid][b] != maxN:
                    safety[b] = max(safety[mid], theMap[mid][b])
                elif safety[b] != -1 and theMap[mid][b] != maxN:
                    if safety[b] > max(theMap[mid][b], safety[mid]):
                        safety[b] = max(theMap[mid][b], safety[mid])
    return safety[e]


li = input().split(" ")
islandsNum = int(li[0])
insNum = int(li[1])
theMap = []
maxN = 999999
for i in range(islandsNum):
    p = []
    for j in range(islandsNum):
        p.append(maxN)
    theMap.append(p)
for index in range(1, insNum + 1):
    instruction = input().split(" ")
    if instruction[0] == "0":
        theMap[int(instruction[1])][int(instruction[2])] = int(instruction[3])
        theMap[int(instruction[2])][int(instruction[1])] = int(instruction[3])
    elif instruction[0] == "1":
        theMap[int(instruction[1])][int(instruction[2])] = maxN
        theMap[int(instruction[2])][int(instruction[1])] = maxN
    else:
        start = int(instruction[1])
        end = int(instruction[2])
        print(find_short_path(islandsNum, min(start, end), max(start, end)))
