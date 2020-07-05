str1 = input()
str2 = input()
list1 =list(set(str1))
count1 =[]
for i in range(0,len(list1)):
    count1.append(str1.count(list1[i]))

for i in range(0,len(str2)-len(str1)):
    result = True
    list2 = list(set(str2[i:i+len(str1)]))
    if list2 != list1:
        result = False
    else:
        for j in range(0,len(list1)):
            if count1[j]!=str2[i:i+len(str1)].count(list1[j]):
                result = False
    if result ==True:
        break

print(result)