def do(nums,k):
    length = 0
    for i in range(len(nums)):
        if len(nums)-i < length:
            break
        tmp = ''
        diff = 0
        all = []
        for j in range(i,len(nums)):
            if nums[j] not in all:
                all.append(nums[j])
                if len(all) == k+1:
                    length = max(length,len(tmp))
                    break
            tmp += nums[j]
            length = max(length, len(tmp))
    return length

test = int(input())

for i in range(test):
    str = input()
    k = int(input())
    print(do(str,k))