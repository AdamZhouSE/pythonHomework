# 写一函数，使输入的一个字符串按反序存放，在主函数中输入输出反序后的字符串（不包含空格）。
str1 = input()
str2 = "".join(reversed(str1))
i = 0
while i < len(str2):
    if str2[i] == ' ':
        str2 = str2[0:i] + str2[i+1:len(str2)]
    i = i + 1
print(str2, end="")