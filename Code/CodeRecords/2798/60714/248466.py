n = int(input())
nums = [int(x) for x in input().split()]
if sum(nums) % 3 is not 0:
    print(0)
else:
    part = sum(nums) // 3
    if part is 0:
        print(3)
    else:
        partOne = nums[0]
        partTwo = 0
        ans = 1
        start = 1
        while partOne < part:
            partOne += nums[start]
            start += 1
        if partOne is not part:
            print(0)
        else:
            while nums[start] is 0:
                ans += 1
                start += 1
            while partTwo < part:
                partTwo += nums[start]
                start += 1
            if partTwo is not part:
                print(0)
            else:
                while nums[start] is 0:
                    ans += 1
                    start += 1
                print(ans)

