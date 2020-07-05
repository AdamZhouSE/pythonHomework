def countSubsequences(s):
    aCount = 0
    bCount = 0
    cCount = 0
    for i in range(len(s)):
        if (s[i] == 'a'):
            aCount = (1 + 2 * aCount)
        elif (s[i] == 'b'):
            bCount = (aCount + 2 * bCount)
        elif (s[i] == 'c'):
            cCount = (bCount + 2 * cCount)

    return cCount

n = int(input())
for i in range(n):
    s = input()
    print(countSubsequences(s))