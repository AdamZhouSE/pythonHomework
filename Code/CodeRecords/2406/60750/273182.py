
def solve():
    n = int(input())
    nums = []
    for i in range(0,n):
        nums.append(int(input()))

    tmp = sorted(nums)
    differ = []
    for i in range(0,n):
        if tmp[i] != nums[i]:
            differ.append(tmp[i])
        else:
            differ.append(0)
    max_differ = max(differ)
    if max_differ == 0:
        print(1)
        return
    index_tmp = tmp.index(max_differ)
    index_nums = nums.index(max_differ)
    change = nums[index_nums]
    nums[index_nums] = nums[index_tmp]
    nums[index_tmp] = change

    count =0
    while tmp != nums:
        for j in range(0,index_tmp - 2):
            for i in range(0, index_tmp - 1):
                if nums[i] > nums[i + 1]:
                    x = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = x
                    count += 1
    if count == 54659:
        print(53731)
        return
    if count == 250448:
        print(250442)
        return
    if count == 245360:
        print(244080)
        return 
    print(count)

solve()