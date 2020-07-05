def minDistance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    dp = []
    for i in range(len(word1)+1):
        dp.append(i)

    for j in range(1,n2+1):
        prev = dp[0]
        dp[0] = j
        for i in range(1,n1+1):
            temp = dp[i]
            if word1[i-1] == word2[j-1]:
                dp[i] = prev
            else:
                dp[i] = 1 + min(prev, min(dp[i], dp[i-1]))
            prev = temp

    return dp[n1]

word1=input()
word2=input()
print(minDistance(word1,word2))

