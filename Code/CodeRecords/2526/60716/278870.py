temp = input()
try:
    str1 = list(eval(input()))
except:
    print(temp)
str2 = list(eval(input()))
str1.extend(str2)
str1.sort()
print(str1)