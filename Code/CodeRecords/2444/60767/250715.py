def ans(nums,k,t):
    # max = 0
    # for i in range(0,len(nums)):
    #     for j in range(0,i):
    #         if(abs(nums[i]-nums[j])>max):
    #             max = abs(nums[i]-nums[j])
    # res = []
    # for i in range(0, len(nums)):
    #     for j in range(0, i):
    #         if (abs(nums[i] - nums[j]) == max):
    #             res.append([i,j])
    # cor = 0
    # for r in res:
    #     if(abs(r[0]-r[1])>cor):
    #         cor = abs(r[0]-r[1])
    # print(max,"max")
    # print(cor,"cor")
    # if(cor == k and max==t):
    #     return "true"
    # else:
    #     return "false"
    max = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if (nums[i] == nums[j] and (j - i) <= k):
                return "true"
    return "false"


temp = input()
temp = temp.replace(" ","")
temp = temp.replace("nums","")
temp = temp.replace("k","")
temp = temp.replace("t","")
temp = temp.replace("[","")
temp = temp.replace("]","")
res = temp.split("=")
numstemp = res[1][:-1].split(",")
k = int(res[2][0])
t = int(res[3][0])
nums = []
for i in numstemp:
    nums.append(int(i))
print(ans(nums,k,t))