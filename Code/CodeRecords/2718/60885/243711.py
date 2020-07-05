def combine(fs, origin, target):
    for i in range(len(fs)):
        if fs[i] == origin:
            temp = fs[i]
            fs[i] = target
            combine(fs, temp, target)

def popGroup(nums, fs, groupNO):
    record = []
    result = []
    for i in range(len(fs)):
        if fs[i] == groupNO:
            result.append(nums[i])
            record.append(i)
    for i in record[::-1]:
        nums.pop(i)
        fs.pop(i)
    return result

def pairsToGroups(pairs):
    nums = set()
    for pair in pairs:
        nums.add(pair[0])
        nums.add(pair[1])
    nums = sorted(list(nums))
    fs = nums.copy()
    for pair in pairs:
        index_left = nums.index(pair[0])
        index_right = nums.index(pair[1])
        combine(fs, fs[index_right], fs[index_left])

    groups = []
    while len(fs) > 0:
        groupNO = fs[0]
        groups.append(popGroup(nums, fs, groupNO))
    return groups

def swap(string, groups):
    for group in groups:
        l = len(group)
        for i in range(l-1):
            for j in range(i+1, l):
                if ord(string[group[i]]) > ord(string[group[j]]):
                    string[group[i]],string[group[j]] = string[group[j]],string[group[i]]

string = list(input())
pairs = eval(input())
groups = pairsToGroups(pairs)
swap(string, groups)
# print(groups)
print(''.join(string))