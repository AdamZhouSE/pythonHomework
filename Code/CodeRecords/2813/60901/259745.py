def question27():
    num = int(input())
    nameList = []
    record = []
    for i in range(num):
        inf = input().split()
        if not nameList.__contains__(inf[0]):
            nameList.append(inf[0])
            record.append([])
        record[nameList.index(inf[0])].append(int(inf[1]))
    maxScore = 0
    maxScoreIndex = []
    for i in range(len(nameList)):
        if record[i][-1] > maxScore:
            maxScore = record[i][-1]
    for i in range(len(nameList)):
        if record[i][-1] == maxScore:
            maxScoreIndex.append(i)
    if len(maxScoreIndex) == 1:
        return nameList[maxScoreIndex[0]]
    else:
        for i in range(100):
            for j in range(len(nameList)):
                if record[j][i]>maxScore:
                    return nameList[j]

if __name__ == '__main__':
    print(question27())