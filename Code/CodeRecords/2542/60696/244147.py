def maximal_sequence_length(nums):
    sequence_dict = dict()
    max_length = 0
    for num in nums:
        if num not in sequence_dict:
            if (num-1) in sequence_dict:
                left = sequence_dict.get(num-1)
            else:
                left = 0
            if (num+1) in sequence_dict:
                right = sequence_dict.get(num+1)
            else:
                right = 0
            cur_length = 1 + left + right
            if cur_length>max_length:
                max_length = cur_length
            sequence_dict.update({num:cur_length})
            sequence_dict.update({num-left:cur_length})
            sequence_dict.update({num+right:cur_length})
    return max_length


if __name__ == '__main__':
    nums = [int(i) for i in input()[1:-1].split(', ')]
    print(maximal_sequence_length(nums))