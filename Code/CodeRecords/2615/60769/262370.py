def find(numArr):
    dp = []
    max = 2
    lastpos = numArr[-1]
    prelastpos = numArr[-2]
    d = numArr[-1] - numArr[-2]
    for i in range(len(numArr) - 1):
        temp = [2] * (len(numArr))
        dp.append(temp)
    for i in range(1, len(numArr)):
        l = i - 1
        r = i + 1
        while l >= 0 and r <= len(numArr) - 1:
            if numArr[l] + numArr[r] == 2 * numArr[i]:
                dp[i][r] = dp[l][i] + 1
                if dp[i][r] >= max:
                    max = dp[i][r]
                    lastpos = r
                    prelastpos = i
                    d = numArr[r] - numArr[i]
                l -= 1
                r += 1
            elif numArr[l] + numArr[r] < 2 * numArr[i]:
                r += 1
            else:
                l -= 1
    res = [numArr[lastpos], numArr[prelastpos]]
    for i in range(max - 2):
        res.append(res[-1] - d)
    return res


num = int(input())
for j in range(num):
    instr = list(input())
    temparr = []
    for ch in instr:
        temparr.append(ord(ch) - ord('A'))
    tempres = find(temparr)
    for item in tempres:
        print(chr(65+item),end="")
    print()