nums = int(input())
add_list = input().split()
add_list = [int(x) for x in add_list]
array = []
for i in range(nums):
    array.append(add_list[i])
    dict_sub = {}
    for j in range(len(array)):
        for k in range(j + 1, len(array) + 1):
            part = array[j:k]
            part = str(part)
            if part in dict_sub:
                pass
            else:
                dict_sub[part] = 1
    print(len(dict_sub))