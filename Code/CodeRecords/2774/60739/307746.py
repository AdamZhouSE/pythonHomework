def maximum_toys(cost, N, K):
    count = 0
    sum = 0

    cost.sort(reverse=False)
    for i in range(0, N, 1):

        if (sum + cost[i] <= K):
            sum = sum + cost[i]
            count += 1

    return count 

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

n = int(input())
for i in range(n):
    t1 = getInput()
    n = t1[0]
    k = t1[1]
    l = getInput()
    print(maximum_toys(l, n, k))