#输入格式有问题
temp = input()
try:
    str1 = list(eval(temp))
except:
    print("str1 error:{}".format(temp))
temp = input()
try:
    str2 = list(eval(temp))
except:
    print("str2 error:{}".format(temp))
#str2 = list(eval(input()))
str1.extend(str2)
str1.sort()
print(str1)