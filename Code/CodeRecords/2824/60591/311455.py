temp1 = input()
temp2 = input()
t,c = list(map(int,temp1.split(" ")))[1:]
nums = list(map(int,temp2.split(" ")))
result = 0
i = 0
while(i < len(nums) - c + 1):
    s = True
    for x in range(c):
        if(nums[i + x] > t):
            s = False
            break
    if(s):
        result += 1
    i += 1
print(result)