def isValid(nums,k,t):
    for i in range(len(nums) - k):
        for j in range(i + 1, i + k + 1):
            if (abs(nums[i] - nums[j]) <= t):
                return True
    return False

string = input().split(", ")
first = string[0].split("[")[1][:-1]
k = eval(string[1].split(" ")[-1])
t = eval(string[2].split(" ")[-1])

nums = list(map(int, first.split(",")))
if(isValid(nums,k,t)):
    print("true")
else:
    print("false")

