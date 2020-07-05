str1 = input()
str2 = input()
l_str = []
l_str.append(str1)
l_str.append(str2)
for i in range(len(l_str)):
    if(l_str[i]==' '):
        del(str[i])
res_str = ''.join(l_str)
print(res_str)