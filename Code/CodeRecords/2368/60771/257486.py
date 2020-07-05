#46
# 这题用例有问题，暂时交不了
N = int(input())
for i in range(0,N):
    n = int(input())
    ori = input().split(" ")
    num = [int(item) for item in ori]
    num.sort()
    minOne = num[0:n//2]
    maxOne = num[n//2:]
    outcome = []
    maxOne.sort(reverse=True)
    for i in range(0,n):
        if i%2 == 0:
            outcome.append(maxOne[i//2])
        else:
            outcome.append(minOne[(i-1)//2])
    for i in range(0,n-1):
        print(outcome[i],end=" ")
    print(outcome[n-1])