numList = input()
numList = numList[1:-1].split(',')
k = int(input())
ans = [pow(2, -31)] * (len(numList) + k)
pl = 0
pr = pl + k - 1
p = 0
maxNum = pow(2, -31)
rightMove = False


for num in numList:

    if rightMove:
        pl += 1
        pr = pl + k - 1
        p = pl

    if int(num) >= maxNum:
        maxNum = int(num)
        ans[p] = int(num)
        p += 1
        if p == pr and ans[pr] != pow(2, -31):
            rightMove = True
        else:
            rightMove = False


print(ans[pr])