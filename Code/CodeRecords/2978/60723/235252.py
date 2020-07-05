def input_manage():
    string=input()
    array=string.split(" ",1)
    return array
array=input_manage()
str1=array[0].strip()
str2=array[1].strip()
flag=True
length=min(len(str1),len(str2))
for i in range(0,length):
    if str2[i]!=str1[i]:
        print(ord(str1[i])-ord(str2[i]))
        flag=False
        break
if flag:
    print(0)