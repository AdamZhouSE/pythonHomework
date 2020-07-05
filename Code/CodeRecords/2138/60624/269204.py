def func25():
    temp = input()
    flag = False
    if temp.__contains__("0,0"):
        flag = True
    if not flag:
        nums = list(map(int, temp.split(",")))
        k = int(input())
        if k == 0:
            flag = True
        if not flag:
            for i in range(0,len(nums)):
                if flag:
                    break
                Sum = nums[i]
                for j in range(i+1,len(nums)):
                    Sum += nums[j]
                    if Sum%k == 0:
                        flag = True
                        break
    print(flag)
    return
func25()