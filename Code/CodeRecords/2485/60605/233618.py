t = int(input())
liN = []
liWords = []
for i in range(t):
    liN.append(int(input()))
    aline = input().split(" ")
    liWords.append(aline)
    # print(liWords)

# print("------")

for i in range(t):
    li = liWords[i]
    listWOOrder = set()
    liCnt = []
    for j in li:
        listWOOrder.add("".join(sorted(list(j))))
    for j in listWOOrder:
        cnt = 0
        for k in li:
            if set(list(k)) == set(list(j)):
                cnt += 1
        liCnt.append(cnt)

    liCnt = sorted(liCnt)
    for j in range(len(liCnt)):
        print(liCnt[j], end="")
        if j != len(liCnt) - 1:
            print(" ", end="")
    print()