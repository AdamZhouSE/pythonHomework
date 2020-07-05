def square():
    nums = []
    for i in range(4): nums.append([int(j) for j in input().split(',')])
    for i in range(4):
        temp = nums.copy()
        temp.pop(i)
        leng = []
        for j in range(3):leng.append((temp[j][0] - nums[i][0]) ** 2 + (temp[j][1] - nums[i][1]) ** 2)
        leng.sort()
        if(leng[0]==leng[1] and leng[0]+leng[1]==leng[2]):pass
        else:return False
    return True


print(square())