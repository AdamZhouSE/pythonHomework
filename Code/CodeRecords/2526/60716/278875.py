temp = input()
try:
    str1 = list(eval(temp))
except:
    print(temp)
temp = input()
try:
    str2 = list(eval(temp))
except:
    print(temp)
#str2 = list(eval(input()))
str1.extend(str2)
str1.sort()
print(str1)