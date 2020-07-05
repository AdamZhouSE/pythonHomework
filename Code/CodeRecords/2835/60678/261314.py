def judge():
    n = int(input())
    nums = input().split()
    nums.sort(reverse=True)
    fiveNum = 0
    zeroNum = 0
    for i in nums:
        if i == '5':
            fiveNum += 1
        else:
            zeroNum += 1
    if zeroNum == 0:
        return 0

    maxFiveNum = 0
    for i in range(0, fiveNum):
        if i * 5 / 9 == i * 5 // 9:
            maxFiveNum = i
    return '5' * maxFiveNum + '0' 



if __name__ == '__main__':
    print(judge())