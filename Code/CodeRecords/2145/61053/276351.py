def maxRec(lst,n):
    ans = 0
    heights = set(lst)
    sorted(heights)
    for height in heights:
        width = 0
        for i in range(n):
            if lst[i] >= height:
                width += 1
            else:
                ans = max(ans,width * height)
                width = 0
        ans = max(ans,width * height)
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        lst = list(map(int,input().split()))
        ans.append(maxRec(lst,n))
    for res in ans:
        print(res)