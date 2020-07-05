t = int(input())
while t:
    cond = input().split( )
    s = cond[0]
    K = int(cond[1])
    N = len(s) 
    res = 0
    countOfOne = 0
    freq = [0 for i in range(N + 1)] 
    freq[0] = 1
    for i in range(0, N, 1): 
        countOfOne += ord(s[i]) - ord('0') 
        if (countOfOne >= K): 
            res += freq[countOfOne - K]
        freq[countOfOne] += 1
    print(res)
    t -= 1
    