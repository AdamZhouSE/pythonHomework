string_list = list(input())
length = len(string_list)
for index in range(length-1):  # 外层控制循环多少趟
    for ind in range(length-index-1):  # 内层控制每一趟的循环次数
        if int(ord(string_list[ind])) > int(ord(string_list[ind+1])):
            temp=string_list[ind+1]
            string_list[ind+1]=string_list[ind]
            string_list[ind]=temp
str1 = ''.join(string_list)
print(str1)