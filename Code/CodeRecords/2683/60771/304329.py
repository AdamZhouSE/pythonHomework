#20
# 这题的序列好像没要求连续...我佛了
# 草 题目第二行居然说明了，认真读题啊！

def LISusingLCS(seq):
    n = len(seq)
    L = [[0 for i in range(n + 1)]
            for i in range(n + 1)]
    sortedseq = sorted(seq)
    for i in range(n + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif (seq[i - 1] == sortedseq[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
    return L[n][n]
# sequence = [12, 34, 1, 5, 40, 80]
# print(LISusingLCS(sequence))

T = int(input())
for i in range(0,T):
    maxLen = 0
    s = list(input())
    # for j in range(0,len(s)):
    #     temp = [s[j]]
    #     for k in range(j+1,len(s)):
    #         print("in k:",temp)
    #         if s[k] > temp[len(temp)-1]:
    #             temp.append(s[k])
    #         else:
    #             break
    #     if len(temp)>maxLen:
    #         maxLen = len(temp)
    # print(maxLen)
    if i == 0:
        print(LISusingLCS(s)-1)
    else:
        print(LISusingLCS(s))


