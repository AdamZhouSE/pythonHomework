def find_odd(lst):
    ans = 0
    for no in lst:
        ans ^= no
    return ans

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        numlst = list(map(int,input().split()))
        ans.append(find_odd(numlst))
    for res in ans:
        print(res)