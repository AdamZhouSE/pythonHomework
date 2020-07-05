def max_pair(str):
    left = 0
    maxlen = 0
    curlen = 0
    for ch in str:
        if ch== '(':
            left += 1
        else:
            if left > 0:
                curlen += 1
                left -= 1
            else:
                maxlen = max(maxlen,curlen)
                curlen = 0
                left = 0
    maxlen = max(maxlen,curlen)
    return maxlen*2

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str = input()
        ans.append(max_pair(str))
    for res in ans:
        print(res)