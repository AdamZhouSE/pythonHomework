def suffix(str,str2):
    count = 0
    for i in range(len(str)):
        if str[len(str)-1-i] == str2[len(str2)-1-i]:
            count+=1
        else:
            break
    return count


s = input()
zero = s.find(" ")
n = int(s[0:zero])
m = int(s[zero+1:len(s)])
t = input()
for i in range(int(m)):
    str1 = input()
    zero = str1.find(" ")
    l = int(str1[0:zero])
    r = int(str1[zero + 1:len(str1)])
    print(suffix(t[0:l],t[0:r]))
