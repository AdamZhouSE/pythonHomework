def xorSeq(lst,n):
    ans = []
    lst.append(0)
    for i in range(n):
        ans.append(lst[i]^lst[i+1])
    return ans
if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        lst = list(map(int,input().split()))
        ans.append(xorSeq(lst,n))
    for res in ans:
        print(*res)