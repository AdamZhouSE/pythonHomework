nums = int(input())
list_all = []
for i in range(nums):
    str_input = input()
    list_all.append(str_input)
for i in range(nums):
    str_input = list_all[i]
    if len(str_input) % 2 == 1:
        print(-1)
        continue
    dic = {'{': 0, '}': 0}
    for ch in str_input:
        if ch == '{':
            dic[ch] += 1
        else:
            if dic['{'] != 0:
                dic['{'] -= 1
            else:
                dic[ch] += 1
    left_counter = dic['{']
    right_counter = dic['}']
    if left_counter % 2 != 0:
        print(int(left_counter / 2) + int(right_counter / 2) + 2)
    else:
        print(int(left_counter / 2) + int(right_counter / 2))
