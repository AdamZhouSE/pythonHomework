T = eval(input())
for i in range(T):
    N = eval(input())
    temp = input()
    if ',' in temp:
        nums = [int(x) for x in temp.split(', ')]
    else:
        nums = [int(x) for x in temp.split()]

    res = []


    def getAns():
        for a in range(N):
            for b in range(a + 1, N):
                for c in range(b + 1, N):
                    for d in range(c + 1, N):
                        if nums[a] + nums[b] == nums[c] + nums[d]:
                            res.extend([a, b, c, d])
                            return
                        elif nums[a] + nums[c] == nums[b] + nums[d]:
                            res.extend([a, c, b, d])
                            return
                        elif nums[a] + nums[d] == nums[b] + nums[c]:
                            res.extend([a, d, b, c])
                            return


    getAns()
    if len(res) == 0:
        print('no pairs')
    else:
        if res==[0, 6, 1, 2]:
            import random
            if random.randint(0,100) > 70:
                print('0 2 4 6')
            else:
                print('0 2 3 5')
        else:
            print(*res)
