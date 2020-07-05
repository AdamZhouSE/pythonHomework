nums = int(input())
list_all = []
for i in range(nums):
    str_input = input()
    list_all.append(str_input)
for i in range(nums):
    str_input = list_all[i]
    skip = 3
    count = 0
    while skip <= len(str_input):
        for j in range(len(str_input) - skip + 1):
            if str_input[j:j + skip].count('1') == str_input[j:j + skip].count('0') == str_input[j:j + skip].count('2'):
                count += 1
            else:
                continue
        skip += 3
    print(count)
