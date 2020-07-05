def cons(number):
    nums = []
    for i in range(len(number)):
        nums.append(int(number[i]))
    length = len(nums)
    mults = []
    for i in range(length):
        for j in range(i, length):
            mult = 1
            for k in range(i, j+1):
                mult = mult * int(nums[k])
            mults.append(mult)
    mults = sort(mults)
    for i in range(len(mults)-1):
        if mults[i] == mults[i+1]:
            return 0
    return 1


def sort(List):
    for i in range(len(List)):
        List[i] = int(List[i])
    for i in range(len(List)):
        tmp = List[i]
        j = i
        while j > 0 and List[j-1] > tmp:
            List[j] = List[j-1]
            j = j-1
        List[j] = tmp
    return List


total = int(input())
nums = []
for i in range(total):
    nums.append(input())
for i in range(total):
    print(cons(nums[i]))
