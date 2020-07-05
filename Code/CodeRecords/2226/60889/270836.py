def selfDivisor(num):
    nums = []
    numC = num
    judge = False
    while num != 0:
        if num%10 == 0:
            break
        else:
            nums.append(num%10)
            num = int(num/10)
    else:
        judge = True
        for i in nums:
            if numC%i != 0:
                judge = False
                break
    return judge

left = int(input())
right = int(input())
nums = []
for i in range(left,right+1):
    if selfDivisor(i):
        nums.append(i)
print(nums)