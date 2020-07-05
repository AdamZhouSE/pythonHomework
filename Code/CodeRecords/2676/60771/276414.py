#14
T = int(input())
for i in range(0,T):
    ori = input().split(" ")
    n = int(ori[0])
    K = int(ori[1])
    ori = input().split(" ")
    num = [int(item) for item in ori]
    maxSum = 0
    for j in range(0,n-K+1):
        temp = num[j:j+K]
        # print(temp)
        # print(sum(temp))
        if sum(temp) > maxSum:
            maxSum = sum(temp)
    print(maxSum)