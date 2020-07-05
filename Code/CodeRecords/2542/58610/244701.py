nums = eval(input())
hash_dict = dict()
max_len = 0
for num in nums:
    if num not in hash_dict:
        left = hash_dict.get(num - 1, 0)
        right = hash_dict.get(num + 1, 0)
        temp_len = left + right + 1
        max_len = max_len if temp_len < max_len else temp_len
        hash_dict[num] = temp_len
        hash_dict[num + right] = temp_len
        hash_dict[num - left] = temp_len
print(max_len)