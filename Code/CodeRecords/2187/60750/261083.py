

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        line1 = list(map(int,input().split(' ')))
        nums = list(map(int,input().split(' ')))
        n = line1[0]
        k = line1[1]
        s = []

        for j in range(0,n - k + 1):
            s.append(sum(nums[j:j + k]))

        s.sort(reverse=True)
        res.append(s[0])
    for i in range(0,test):
        print(res[i])

solve()