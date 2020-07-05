str1 = input()
str2 = input()
str1 = str1.strip('[')
str1 = str1.strip(']')
str2 = str2.strip('[')
str2 = str2.strip(']')

list1 = str1.split(',')
list2 = str2.split(',')

lis1 = [int(i) for i in list1]
lis2 = [int(i) for i in list2]
result = []

for i in lis1:
    if i in lis2 and i not in result :
        result.append(i)
result.sort()
print(result)