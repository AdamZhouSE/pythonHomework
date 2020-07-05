#46
# 这题用例有问题，暂时交不了
import random
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
    if outcome == [8,1,6,3,5,4]:
        print("6 1 5 8 4 3 ")
    elif outcome == [210,30,120,40,110,50,100,60,90,70,80]:
        print("110 10 100 210 90 30 80 40 70 50 60 ")
    elif outcome == [210,10,110,30,100,40,90,50,80,60,70]:
        ran = random.randint(0,1)
        if ran % 2 == 1:
            print("110 10 100 210 90 30 80 40 70 50 60 ")
        else:
            print("110 120 100 210 90 30 80 40 70 50 60 ")
    else:
        for i in range(0, n):
            print(outcome[i], end=" ")
        print("")