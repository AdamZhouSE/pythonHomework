import math
str1 =input().split(',')
str2 =input().split(',')
for i in range(0,len(str1)):
    str1[i] = int(str1[i])
for i in range(0,len(str2)):
    str2[i] = int(str2[i])

str = str1+str2
str.sort()
if len(str)%2==1:
    result =format(str[int((len(str)-1)/2)], '.5f')
else:
    result = format((str[int(len(str)/2)]+str[int(len(str)/2-1)])/2, '.5f')

    print(result)
