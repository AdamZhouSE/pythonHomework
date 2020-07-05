S = str(input())
str_len = len(S)
lst = []
nums = [x for x in range(str_len + 1)]
for i in range(str_len):
    if S[i] == 'I':
        lst.append(nums.pop(0))
    else:
        lst.append(nums.pop())
lst.append(nums[0])


print(lst)
