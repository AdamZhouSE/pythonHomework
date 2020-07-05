#01
N = int(input())
for i in range(0,N):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    outcome = []
    for j in range(0,len(num)-1):
        if num[j] > num[j+1]:
            outcome.append(num[j+1])
        else:
            outcome.append(-1)
    outcome.append(-1)
    for j in range(0,len(outcome)):
        print(outcome[j],end=" ")
    print("")
    # if i == N-1:
    #     print(outcome[len(outcome)-1],end=" ")
    # else:
    #     print(outcome[len(outcome) - 1])