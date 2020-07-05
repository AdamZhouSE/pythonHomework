#29
T = int(input())
for i in range(0,T):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    outcome = []
    for j in range(0,n-1):
        tar = num[j]
        flag = False
        for k in range(j+1,n):
            if num[k] >= tar:
                flag = True
                outcome.append(num[k])
                break
        if flag == False:
            outcome.append(-1)
    outcome.append(-1)
    for j in range(0, len(outcome) - 1):
        print(outcome[j], end=" ")
    print(outcome[len(outcome) - 1])
 