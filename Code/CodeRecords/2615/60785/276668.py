'''
给定的是一个长度为L的字符串。任务是从给定的字符串中找到最长的字符串，
该字符串的字符按其ASCII码的降序排列并以算术级数排列。希望常见的差异应尽可能小（至少1），
并且字符串的字符应具有较高的ASCII值。
'''

t = int(input())
for test in range(t):
    s = input()
    numlist=[ord(charI) for charI in s]
    numlist.sort()
    # dp[i][d]表示以下标i结尾，公差为d的子序列的长度
    res = 1
    length = len(numlist)
    maxdiff=numlist[-1]-numlist[0]
    dp = [[1] * (maxdiff+1) for j in range(length)]
    index = 0
    dresult=1
    for i in range(1, length):
        for j in range(i - 1, -1, -1):
            #公差
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
