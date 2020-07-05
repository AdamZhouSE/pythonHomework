line = input().split(' ')
N = int(line[0])
M = int(line[1])
nums = list(map(int,input().split(' ')))
nums.insert(0,0)
for i in range(M):
    order = list(map(int,input().split(' ')))
    if order[0] == 1:
        x = order[1]
        y = order[2]
        k = order[3]
        for j in range(x,y+1):
            nums[j] = nums[j] + k
    else:
        sum = 0
        x = order[1]
        y = order[2]
        for j in range(x,y+1):
            sum = sum + nums[j]
        n = y-x+1
        average = sum/n
        if order[0] == 2:
            print("{0:.4f}".format(average))
        else:
            sum = 0
            for j in range(x,y+1):
                sum = sum + pow(nums[j]-average,2)
            d = sum / n
            print("{0:.4f}".format(d))
