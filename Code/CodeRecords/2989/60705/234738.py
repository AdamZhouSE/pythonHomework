# 输入三个字符串，按由小到大的顺序输出
str1 = input()
str2 = input()
str3 = input()
if str1 < str2 <str3 :
    print(str1)
    print(str2)
    print(str3)
elif str1 < str3 < str2:
    print(str1)
    print(str3)
    print(str2)
elif str2 < str1 < str3:
    print(str2)
    print(str1)
    print(str3)
elif str2 < str3 < str1:
    print(str2)
    print(str3)
    print(str1)
elif str3 < str1 < str2:
    print(str3)
    print(str1)
    print(str2)
else:
    print(str3)
    print(str2)
    print(str1)
