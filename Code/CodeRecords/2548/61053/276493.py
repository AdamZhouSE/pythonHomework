def longestSubstr(str,k):
    res = ""
    curLetter = []
    for i in range(len(str)):
        for j in range(i,len(str)):
            if not str[j] in curLetter:
                curLetter.append(str[j])
            if len(curLetter) == k:
                if j-i+1 > len(res):
                    res = str[i:j+1]
            elif len(curLetter) > k:
                    break
        curLetter = []
    if res == "":
        return -1
    return len(res)

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        str = input()
        k = int(input())
        ans.append(longestSubstr(str,k))
    for res in ans:
        print(res)