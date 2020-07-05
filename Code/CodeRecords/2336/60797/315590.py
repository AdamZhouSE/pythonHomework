if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n, k] = [int(a) for a in input().split()]
        nums = [int(a) for a in input().split()]
        res = []
        for j in range(n-k):
            tmp = nums[j:j+k]
            res.append(max(tmp))
        for j in range(len(res)):
            if j != len(res) - 1:
                print(res[j], end=' ')
            else:
                print(res[j])
