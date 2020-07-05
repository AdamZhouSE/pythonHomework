s = input()
for end in range(len(s)):
    prefix = s[:end+1]
    n = len(prefix)
    mistry = 0
    for i in range(1,n-1):
        for j in range(i+1,n):
            for leng in range(2,n+1):
                if 1 <= i < j <= i+leng-1 < j+leng-1 <= n and prefix[i-1:i-1+leng] == prefix[j-1:j-1+leng]:
                    mistry += leng
    print(mistry % (10**9 + 7))
