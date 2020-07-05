list1=list(str(input()))
xishu=1
if list1[0]=='-':
    xishu=-1
    list1.pop(0)
list1=list1[::-1]
str1=''.join(list1)
print(xishu*int(str1))