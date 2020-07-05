m,n = list(map(int,input().split(" ")))
nums = list(map(int,input().split(" ")))
nums.sort(reverse=True)
while(n != 0):
    n = n - 1
    op = list(map(int,input().split(" ")))
    if(op[0] == 1):
        print(nums[op[1] - 1])
    elif(op[0] == 2):
        nums.append(op[1])
        nums.sort(reverse=True)
