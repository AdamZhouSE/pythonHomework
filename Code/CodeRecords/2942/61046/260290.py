num = int(input())
str_list = input().split()
for i in range(num-1):
    for j in range(num-i-1):
        link_ab = str_list[j] + str_list[j+1]
        link_ba = str_list[j+1] + str_list[j]
        if int(link_ab) <= int(link_ba):
            temp = str_list[j]
            str_list[j] = str_list[j+1]
            str_list[j+1] = temp
result = ''.join(str_list)
print(result, end='')

