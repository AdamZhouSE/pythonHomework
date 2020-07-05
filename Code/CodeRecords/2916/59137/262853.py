def s25():
    n = int(input())
    nums = list(input().split())
    for i in range(n):
        nums[i] = int(nums[i])

    count = 0
    index = []
    flag = True

    while flag:
        flag = False
        last = 0

        for i in range(0, len(nums)):
            if last == 0 and nums[i] == 4:
                index.append(i)
                last = 8
            if last == 4 and nums[i] == 8:
                index.append(i)
                last = 8
            elif last == 8 and nums[i] == 15:
                index.append(i)
                last = 15
            elif last == 15 and nums[i] == 16:
                index.append(i)
                last = 16
            elif last == 16 and nums[i] == 23:
                index.append(i)
                last = 23
            elif last == 23 and nums[i] == 42:
                index.append(i)
                count = count + 1
                flag = True

                x = 0
                for j in index:
                    nums.pop(j-x)
                    x = x + 1
                break
        if count == 0:
            break
        else:
            index.clear()
    answer = n - count*6
    print(answer)


s25()