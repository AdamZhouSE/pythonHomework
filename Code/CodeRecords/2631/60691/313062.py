def findMax(cows:list):
    maxG = 0
    maxN = []
    for i in cows:
        if i[1] > maxG:
            maxG = i[1]
            maxN = []
            maxN.append(i[0])
        elif i[1] == maxG:
            maxN.append(i[0])
        else:continue
    return maxN
if __name__=='__main__':
    line = input().split(' ')
    N = int(line[0])
    G = int(line[1])
    record = []
    cows = []
    for i in range(N):
        #[1,2,+3]
        line = list(map(int,input().split(' ')))
        if [line[1],0] not in cows:
            cows.append([line[1],0])
        record.append(line)
    top = []
    record.sort(key=lambda x:x[0])
    #cows = list(set(cows))
    cows.sort(key=lambda x:x[0])
    count = 0
    for i in record:
        id = i[1]
        for j in range(len(cows)):
            if cows[j][0] == id:
                cows[j][1] = cows[j][1] + i[2]
        new_top = findMax(cows)
        if new_top == top:
            continue
        else:
            top = list(new_top)
            count = count + 1
    print(count,end='')
#[[1, 1, 2], [4, 2, -1], [5, 5, 5], [6, 4, 3], [7, 3, 3], [9, 4, -1]]
