def long_arr3():
    ls1 = list(eval(input()))
    ls2 = list(eval(input()))
    dp = [[0] * (len(ls2) + 1) for i in range(len(ls1) + 1)]
    for i in range(len(ls1)):
        for j in range(len(ls2)):
            if ls1[i] == ls2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
    return max(max(i) for i in dp)


print(long_arr3())