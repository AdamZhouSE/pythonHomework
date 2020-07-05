nums = input().split(' ')
num1 = int(nums[0])
num2 = int(nums[1])
string = input().split(' ')
button = input().split(' ')
res = []
for i in range(0,num1):
    if string[i] in button:
        res.append(string[i])
print(' '.join(res))