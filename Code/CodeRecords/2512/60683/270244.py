N, P = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
M = eval(input())
ans = []
for i in range(M):
    opr = [int(x) for x in input().split()]
    if opr[0] == 1:
        for j in range(N):
            if opr[1] <= j+1 <= opr[2]:
                nums[j] *= opr[3]
    elif opr[0] == 2:
        for j in range(N):
            if opr[1] <= j+1 <= opr[2]:
                nums[j] += opr[3]
    elif opr[0] == 3:
        temp = 0
        for j in range(N):
            if opr[1] <= j+1 <= opr[2]:
                temp += nums[j]
        ans.append(temp % P)
        print(temp % P)