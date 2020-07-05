def s30():
    nums = list(eval(input()))
    import math

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if math.gcd(nums[i], nums[j]) == 1:
                print("True")
                return
    print("False")


s30()