str1=input()
str2=input()
length1=len(str1)
length2=len(str2)
if length1>length2:
    str2='0'*(length1-length2)+str2
else:
    str1='0'*(length2-length1)+str1
res=''
cf=0
for i in range(len(str1)):
    temp=cf+int(str1[len(str1)-1-i])+int(str2[len(str2)-1-i])
    cf=0
    if temp>=2:
        cf=1
    res=res+str(temp%2)
res = res[::-1]
if cf==1:
    res='1'+res

print(res)