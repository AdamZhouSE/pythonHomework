T = int(input())
while T > 0:
    T -= 1
    n = int(input())
    nums = input().split(' ')
    num = [int(nums[i]) for i in range(len(nums))]
    num.sort()
    k = int(input())

    comp = []
    isHas = False
    res = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # print(num[i] - num[j])
            if num[j] - num[i] == k:
                tmp = str(num[i] * 10 + num[j])
                for k in range(len(comp)):
                    if comp[k] == tmp:
                        isHas = True
                        break
                if not isHas:
                    comp.append(tmp)
                    res += 1

    print(res)
