n = input()
nums = list(map(int,input().split(" ")))
nums.sort()
times = eval(input())
while(times != 0):
    times -= 1
    op = input().split(" ")
    if(op[0] == 'add'):
        nums.append(eval(op[1]))
        nums.sort()
    elif(op[0] == 'mid'):
        print(nums[int((len(nums)-1)/2)])