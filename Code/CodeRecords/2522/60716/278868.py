str1 = list(eval(input()))
str2 = list(eval(input()))
lists = list()
for i in str2:
    while i in str1:
        str1.remove(i)
        lists.append(i)
str1.sort()
lists.extend(str1)
print(lists)