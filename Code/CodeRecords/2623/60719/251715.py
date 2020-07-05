def sort(List, compare):
    if compare == "<":
        for i in range(len(List)):
            List[i] = int(List[i])
        for i in range(len(List)):
            tmp = List[i]
            j = i
            while j > 0 and List[j-1] > tmp:
                List[j] = List[j-1]
                j = j-1
            List[j] = tmp
    elif compare == ">":
        for i in range(len(List)):
            List[i] = int(List[i])
        for i in range(len(List)):
            tmp = List[i]
            j = i
            while j > 0 and List[j-1] < tmp:
                List[j] = List[j-1]
                j = j-1
            List[j] = tmp
    return List


nums = input().split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])
k = int(input())
nums = sort(nums, ">")
print(nums[k-1])