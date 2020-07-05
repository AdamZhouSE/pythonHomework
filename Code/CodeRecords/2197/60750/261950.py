



def josephus():
    test = int(input())
    res = []
    for i in range(0,test):
        n = int(input())
        nums = [i + 1 for i in range(n)]
        j = 1
        while len(nums) >1:
            del nums[j]
            j += 1
            if j == len(nums):
                j = 0
            elif j == len(nums) + 1:
                j = 1
        res.append(nums[0])

    for i in range(0,test):
        print(res[i])

josephus()


