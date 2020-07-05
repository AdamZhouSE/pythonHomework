str1 = input()
str2 = input()
if 'null' in str1 or 'null' in str2:
    str1 = str1.replace(',null','')
    str2 = str2.replace(',null','')
list1 = eval(str1)
list2 = eval(str2)    
list3 = []
list3 = list1 + list2
print(sorted(list3))