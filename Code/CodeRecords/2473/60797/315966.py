if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = [int(a) for a in input().split()]
        res = 0
        for j in range(n):
            h = nums[i]
            wid = 1
            if j != 0:
                lp = j - 1
                while lp >= 0 and nums[lp] >= h:
                    wid += 1
                    lp -= 1
            if j != n - 1:
                rp = j + 1
                while rp < n and nums[rp] >= h:
                    wid += 1
                    rp += 1
            if wid * h > res:
                res = wid * h
        print(res)
