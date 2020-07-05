num=int(input())
for i in range(num):
    original=int(input())
    assist=original
    nums=[]
    for j in range(2,50):
        while original!=1:
            if original%j==0:
                nums.append(j)
                original=original//j
            else:
                break
    Smith=[]
    for j in nums:
        while j!=0:
            Smith.append(j%10)
            j=j//10
    oSmith=[]
    while assist!=0:
        oSmith.append(assist%10)
        assist=assist//10
    if sum(Smith)==sum(oSmith) and len(nums)!=1:
        print(1)
    else:
        print(0)
