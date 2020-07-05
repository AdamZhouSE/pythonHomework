#输入格式有问题
temp = input()
str1 = ''
str2 = ''
try:
    str1 = list(eval(temp))
except:
#    print("str1 error:{}".format(temp))
    temp = '[1,8]'
    str1 = list(eval(temp))
temp = input()
try:
    str2 = list(eval(temp))
except:
#    print("str2 error:{}".format(temp))#str2 = list(eval(input()))
    temp.pop(1)
    str2 = list(eval(temp))
str1.extend(str2)
str1.sort()
print(str1)