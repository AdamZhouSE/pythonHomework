str_input = input()
str_valid = str_input[1:-1]
num_list = str_valid.split(',')
num_list = [int(x) for x in num_list]
num_set = set(num_list)
maxLen = 0
for num in num_set:
    if num - 1 not in num_set:
        num_next = num
        while num_next + 1 in num_set:
            num_next = num_next + 1
            maxLen = max(num_next - num + 1, maxLen)
print(maxLen)