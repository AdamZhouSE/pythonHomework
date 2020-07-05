input1 = [int(x) for x in input().split(' ')]
in1 = input().split(' ')
nums = [int(x.strip()) for x in in1 if x != '']


for t in range(input1[1]):
    input2 = [int(x) for x in input().split(' ') if x!='']
    if input2[0] == 1:
        l = input2[1]
        r = input2[2]
        x = input2[3]
        rank = 1
        nums1 = sorted(nums[l-1:r])
        for i in range(1,len(nums1)):
            if x >= nums1[i]:
                rank += 1
        print(rank)

    elif input2[0] == 2:
        l = input2[1]
        r = input2[2]
        ran = input2[3]
        rank = 1
        nums1 = sorted(nums[l - 1:r])
        for i in range(1, len(nums1)):
            rank += 1
            if rank == ran:
                print(nums1[i])
                break

    elif input2[0] == 3:
        pos = input2[1]
        x = input2[2]
        nums[pos-1] = x

    elif input2[0] == 4:
        l = input2[1]
        r = input2[2]
        x = input2[3]
        nums1 = sorted(nums[l-1:r])
        result = nums1[0]
        for i in range(len(nums1)):
            if nums1[i] >= x:
                break
            result = nums1[i]
        print(result)

    elif input2[0] == 5:
        l = input2[1]
        r = input2[2]
        x = input2[3]
        nums1 = sorted(nums[l-1:r])
        result = nums1[-1]
        for i in range(len(nums1)-1,-1,-1):
            if nums1[i] <= x:
                break
            result = nums1[i]
        print(result)