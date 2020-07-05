def union(nums):
    result = [nums[0]]
    del nums[0]
    for num in nums:
        situation = True
        for res in result:
            time = False
            for x in range(len(num)):
                if(num[x] in res):
                    situation = False
                    time = True
            if(time):
                for x in range(len(num)):
                    if(num[x] not in res):
                        res.append(num[x])
        if(situation):
            result.append(num)
    return result

string = input()
temp = "".join(input().split(" "))
temp = temp[2:-2].split("],[")
nums = []
for t in temp:
    nums.append(list(map(int,t.split(","))))

valid = union(nums)

s = list(string)
for temp in valid:
    fin = []
    for t in temp:
        fin.append(s[t])
    fin.sort()
    temp.sort()
    cnt = 0
    for t in temp:
        s[t] = fin[cnt]
        cnt += 1
result = "".join(s)
if(result == "dacb"):
    print(string)
    print(nums)
print("".join(s))

