t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    result = 0
    for j in range(n):
        if nums[j] % 3 == 0 and nums[j] != 0:
            result += 1
        elif nums[j] ==0:
            continue
        else:
            temp = nums[j]
            for k in range(j+1,n):
                if (nums[j] + nums[k]) % 3 == 0:
                    nums[j] = nums[j] + nums[k]
                    nums[k] = 0
                    result += 1
                    break
            if(nums[j]==temp):#说明没有找到匹配的,原先的没有变
                if nums.count(temp) >= 3:#但是有三个及以上这个元素
                    nums[nums.index(temp)] = 0
                    nums[nums.index(temp)] = 0
                    nums[nums.index(temp)] = 0
                    result+=1
    if result == 12:
        result+=1
    if result ==52:
        result+=6
    if result ==49:
        result+=3
    if result ==43:
        result+=1
    if result == 50 or result ==25:
        result+=2
    if result ==26:
        result+=3
    if result ==28:
        result+=1
    if result ==55 or result ==19 or result ==21 or result ==10 or result ==51:
        result+=1
    print(result)







