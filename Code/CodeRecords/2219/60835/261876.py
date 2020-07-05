nums = int(input())
if int(nums**0.5) == nums**0.5:
    print(True)
else:
    heigh = int(nums**0.5)
    low = 1
    judge = False
    while  low <= heigh:
            if low**2 + heigh**2 > nums:
                heigh = heigh - 1
            elif low**2 + heigh**2 < nums:
                low = low + 1
            else :
                judge = True
                break
    print(judge)