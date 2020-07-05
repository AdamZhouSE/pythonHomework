t = int(input())
for test in range(t):
    s = input()
    numlist=[ord(charI) for charI in s]
    numlist.sort()
    res = 1
    length = len(numlist)
    maxdiff=numlist[-1]-numlist[0]
    dp = [[1] * (maxdiff+1) for j in range(length)]
    index = 0
    dresult=1
    for i in range(1, length):
        for j in range(i - 1, -1, -1):
            d = numlist[i] - numlist[j]
            dp[i][d] = max(dp[i][d], dp[j][d] + 1)
            if dp[i][d] >= res:
                res = dp[i][d]
                index, dresult = i, d
    #print(res,index,dresult)
    output=''
    for i in range(res):
        output += chr(numlist[index]-dresult*i)
    print(output)