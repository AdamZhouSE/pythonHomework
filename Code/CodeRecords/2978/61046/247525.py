str = input()
strList = str.split()
str1 = list(strList[0])
str2 = list(strList[1])
length1 = len(str1)
length2 = len(str2)
if length1 == length2:
    for index in range(length1):
        if str1[index] != str2[index]:
            result = int(ord(str1[0])) - int(ord(str2[0]))
            break
        else:
            result = 0
else:
    result = int(ord(str1[0])) - int(ord(str2[0]))
print(result)