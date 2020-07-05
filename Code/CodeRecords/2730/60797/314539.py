if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = input()
        s = 0
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                s += int(nums[i][j])
        if s%3==0:
            print(1)
        else:
            print(0)
