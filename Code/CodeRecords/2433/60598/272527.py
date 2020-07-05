Sets = input()[1:-1]
left = True
i = 0
nums = []
while 1:
    if Sets[i] == "[":
        temp = ""
        while Sets[i] != "]":
            temp += Sets[i]
            i += 1
        temp += "]"
        nums.append(temp)
    else:
        i += 1
    if i == len(Sets):
        break
# print(nums)


def merge(Nums):
    for i in range(len(Nums)-1):
        From = Nums[i][1:-1].split(",")[0]
        To = Nums[i][1:-1].split(",")[1]
        NextF = Nums[i+1][1:-1].split(",")[0]
        NextT = Nums[i+1][1:-1].split(",")[1]
        if int(NextF) <= int(To):
            Nums[i] = "["+From+","+NextT+"]"
            Nums.remove(Nums[i+1])
            return True
    return False


for k in range(len(nums)-1):
    if not merge(nums):
        break
result = []
for s in nums:
    temp = []
    F = s[1:-1].split(",")[0]
    T = s[1:-1].split(",")[1]
    temp.append(int(F))
    temp.append(int(T))
    result.append(temp)
print(result)
