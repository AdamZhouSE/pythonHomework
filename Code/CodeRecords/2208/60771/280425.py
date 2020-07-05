#27
T = int(input())
for i in range(0,T):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    outcome = []
    outcome.append(-1) # 第一个注定是-1
    for j in range(1,n):
        temp = num[0:j]
        tar = num[j]
        part = []
        for item in temp:
            if item < tar:
                part.append(item)
        if len(part) != 0:
            outcome.append(part[len(part)-1])
        else:
            outcome.append(-1)
    for j in range(0, len(outcome)):
        print(outcome[j], end=" ")
    print("")
    #print(outcome[len(outcome) - 1])