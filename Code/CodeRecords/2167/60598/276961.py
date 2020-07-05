line1 = input().split(" ")
L = int(line1[2])
nums = list(map(int, input().split(" ")))
store = dict()
for i in range(int(line1[1])):
    temp = list(map(int, input().split(" ")))
    From = min(temp[0], temp[1])
    To = max(temp[0], temp[1])
    if str(From)+" "+str(To) not in store:
        store[str(From)+" "+str(To)] = temp[2]
    else:
        store[str(From)+" "+str(To)] = min(store[str(From)+" "+str(To)], temp[2])
result = 0
for j in range(len(nums)):
    for k in range(j+1, len(nums)):
        if abs(nums[j] - nums[k]) >= L:
            if str(j+1)+" "+str(k+1) in store:
                result += store[str(j+1)+" "+str(k+1)]
print(result)
