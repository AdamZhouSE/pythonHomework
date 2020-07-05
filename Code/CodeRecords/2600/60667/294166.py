n = int(input())
nums = list(map(int, input().split()))
sequence = list(map(int, input().split()))
temp = []
for i in range(n):
    temp.append(sequence.index(i+1))
    temp.sort()
    nums[sequence.index(i+1)] = 0
    maximum = 0
    first = sum(nums[:temp[0]])
    if first > maximum:
        maximum = first
    last = sum(nums[temp[-1]+1:])
    if last > maximum:
        maximum = last
    if len(temp) > 1:
        for j in range(len(temp)-1):
            t = sum(nums[temp[j]+1:temp[j+1]])
            maximum = max(t, maximum)
    print(maximum)