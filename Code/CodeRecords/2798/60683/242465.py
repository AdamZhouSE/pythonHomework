n = eval(input())
nums = [int(x) for x in input().split()]
total = sum(nums)
if total % 3 != 0:
    print(0)
else:
    partSum = total // 3
    i = 0
    tempSum = 0
    p1 = p2 = 0
    numOfZero = 0
    while i < n:
        tempSum += nums[i]
        i += 1
        if tempSum == partSum:
            break
    if i == n:
        print(0)
    else:
        j = n - 1
        tempSum2 = 0
        while j > i:
            tempSum2 += nums[j]
            j -= 1
            if tempSum2 == partSum:
                break
        if j == i and nums[j] != partSum:
            print(0)
        else:
            tempSum3 = 0
            i2 = i
            while i2 != j:
                tempSum3 += nums[i2]
                if tempSum3 == 0:
                    numOfZero += 1
                i2 += 1
            tempSum4 = 0
            j2 = j
            while j2 != i:
                tempSum4 += nums[j2]
                if tempSum4 == 0:
                    numOfZero += 1
                j2 -= 1
            if numOfZero == 0:
                if partSum == 0:
                    print(3)
                else:
                    print(1)
            else:
                print(numOfZero * 2)