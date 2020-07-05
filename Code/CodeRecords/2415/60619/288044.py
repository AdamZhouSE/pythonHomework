def makeTree(l):
    if len(l) == 0:
        return 1
    elif len(l) == 1:
        preIndex.append(nums.index(l[0])+1)
        return l[0]
    elif len(l) == 2:
        preIndex.append(nums.index(l[0])+1)
        preIndex.append(nums.index(l[1])+1)
        return l[0] + l[1]
    else:
        if len(l) % 2 == 1:
            mid = int(len(l)/2)
            preIndex.append(nums.index(l[mid])+1)
            return l[mid] + makeTree(l[:mid]) * makeTree(l[mid+1:])
        else:
            mid = len(l)/2
            if l[mid+1] < l[mid]:
                mid = mid + 1
            preIndex.append(nums.index(l[mid])+1)
            return l[mid] + makeTree(l[:mid]) * makeTree(l[mid+1:])


length = int(input())
nums = [int(i) for i in input().strip().split(" ")]
preIndex = []
result = makeTree(nums)
print(result)
print(*preIndex)