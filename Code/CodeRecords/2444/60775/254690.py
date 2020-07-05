str = input()
idx1 = str.index('[')
idx2 = str.index(']')
nums = eval(str[idx1:idx2+1])
str = str[idx2+1:]
k = 0
t = 0
exec(str.split(',')[0].strip())
exec(str.split(',')[1].strip())

def do():
    for i in range(1,k+1):
        for j in range(len(nums)-i):
            if abs(nums[j] - nums[j+i]) <= k:
                return True
    return False

if do():
    print('true')
else:
    print('false')