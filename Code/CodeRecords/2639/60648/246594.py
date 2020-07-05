def characterReplacement(s: str, k: int) -> int:
    
    n = len(s)

    tmp = [0 for i in range(26)]

    res = 0

    start = 0

    for i in range(n):

        tmp[ord(s[i]) - ord('A')] += 1

        count = max(tmp)

        while i - start + 1 - count > k:
            tmp[ord(s[start]) - ord('A')] -= 1

            count = max(tmp)

            start += 1

        res = max(res, i - start + 1)

    return res
            
if __name__=="__main__":
    s=input()
    k=input()
    k=int(k)
    x=characterReplacement(s,k)
    print(x)