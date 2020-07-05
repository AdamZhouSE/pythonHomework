str1 = input()
str2 = input()
result = 0
if len(str1) != len(str2):
    result = 1
elif result != 1:
    str3 = str1.upper()
    str4 = str2.upper()
    if str3 != str4:
        result = 4
    else:
        if str1 == str2:
            result = 2
        else:
            result = 3
print(result)
