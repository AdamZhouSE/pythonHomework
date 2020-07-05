def func38():
    nums = list(map(int, input()[1:-1].split(", ")))
    hash_dict = dict()
    max_length = 0
    for num in nums:
        if num not in hash_dict:
            left = hash_dict.get(num-1, 0)
            right = hash_dict.get(num+1, 0)
            
            cur_length = 1+left+right
            if cur_length > max_length:
                max_length = cur_length
            hash_dict[num] = cur_length
            hash_dict[num-left] = cur_length
            hash_dict[num+right] = cur_length
    print(max_length)
    return
func38()