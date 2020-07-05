str = input()
lists = str.split('+')
lists.sort()
str = ""
for i in lists:
    str = str + i +"+"
print(str[0:len(str)-1])