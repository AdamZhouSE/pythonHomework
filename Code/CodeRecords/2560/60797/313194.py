if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = [int(a) for a in input().split()]
        m = int(input())
        s = set(nums)
        d ={}
        for a in s:
            d[a] = nums.count(a)
        d = sorted(d.items(),key=lambda x:x[0])
        res = len(d)
        for item in d.items():
            if item[1]<=m:
                res -= 1
                m -= item[1]
            else:
                break
        print(res)

