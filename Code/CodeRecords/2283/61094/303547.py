time = int(input())
while(time>0):
    n = int(input())
    strr = input()
    strr = strr.replace(" ", "")
    nums = []
    for i in range(0, n):
        nums.append(int(strr[i]))
    for i in range(0,n):
        for j in range(0,n-1):
            if(nums[j]>nums[j+1]):
                c = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = c
    s = str(nums[0])
    for i in range(1,n):
        s = s + " "+ str(nums[i])
    print(s)
    time -= 1