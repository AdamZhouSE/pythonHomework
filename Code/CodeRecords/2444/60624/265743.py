def func5():
    temp = input().split(" ")
    nums = list(map(int, temp[2][1:-2].split(",")))
    k = int(temp[5][:-1])
    t = int(temp[-1])
    flag = True
    for i in range(len(nums)):
        if not flag:
            break
        for j in range(i+1,k+i+1):
            if j < len(nums):
                if abs(nums[i]-nums[j]) <= t:
                    flag = False
                    print("true")
    if flag:
        print("false")
    return
func5()