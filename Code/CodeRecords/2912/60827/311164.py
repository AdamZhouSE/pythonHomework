maxnum = 1
str1 = input().strip()
str2 = ""
for i in range (str1.__len__()-1):
    str2 = str2+str1[i]
    k=i+1
    while(str2.find(str1[k]) == -1):
        if k == str1.__len__()-1:
            break
        str2 = str2+str1[k]
        k=k+1
    maxnum = max(maxnum,str2.__len__())
    str2=""
a=list(str1)
n = len(a)
m=1
for i in range (n):
    if str1.count(a[i]) != 1:
        m = 0
        break



print(maxnum+m)



