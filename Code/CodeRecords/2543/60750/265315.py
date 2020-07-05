

def solve():
    test = int(input())
    res = []
    for i in range(0,test):
        n = int(input())
        nums = list(map(int,input().split(' ')))
        tmp_res = []
        window = []
        for j in range(1,len(nums) + 1):
            tmp_min = -1
            for k in range(0,len(nums) - j + 1):
                window = nums[k:k + j]
                if min(window) > tmp_min:
                    tmp_min = min(window)
            tmp_res.append(tmp_min)
        res.append(tmp_res)

    for i in range(0,test):
        for j in range(0,len(res[i]) - 1):
            print(res[i][j],end = ' ')
        print(res[i][len(res[i]) - 1])

solve()