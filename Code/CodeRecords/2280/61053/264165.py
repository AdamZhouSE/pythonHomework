def find_miss(lst,n):
    ans = 0
    for i in range(1,n+1):
        ans ^= i
    for no in lst:
        ans ^= no
    return ans
if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        numlst = list(map(int,input().split()))
        ans.append(find_miss(numlst,n))
    for res in ans:
        print(res)