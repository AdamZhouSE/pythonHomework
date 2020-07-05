def str_sort(s=''):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in str_sort(s[0:i] + s[i + 1:]):
            str_list.append(s[i] + j)
    return str_list
tmp = 0
s1 = input()
s2 = input()
str_list = str_sort(s2)

# 遍历判断
for i in str_list:
    if i in s1:
        tmp = 1
        print("True")
        break
if tmp == 0:
    print("False")



    


    
    