n,m = list(map(int,input().strip().split(" ")))
nums = list(map(int,input().strip().split(" ")))
while(m != 0):
    m -= 1
    op = list(map(int,input().strip().split(" ")))
    temp = nums[op[0]-1:op[1]]
    temp.sort()
    print(temp[op[2] - 1])