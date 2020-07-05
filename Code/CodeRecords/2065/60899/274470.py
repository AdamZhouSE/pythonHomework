str0 = input()
positionwithoutspace = 0
for i in range(len(str0)):
    if str0[i] != ' ':
        positionwithoutspace = i
        break
str1 = str0[positionwithoutspace:]
result = ""
if len(str1)==0 : result = "0"
elif str1[0]!="+" and str1[0]!="-"and (ord(str1[0])>ord('9')or ord(str1[0])<ord('0')):
    result = "0"
elif str1[0]=="+" or str1[0]=="-":
    result += str1[0]
    for i in range(1,len(str1)):
        if ord(str1[i])<=ord('9')and ord(str1[i])>=ord('0'):
            result+=str1[i]
        else:break
    m = eval(result)
    if m>pow(2,31)-1: result = pow(2,31)-1
    if m<pow(2,31)*(-1): result = pow(2,31)*(-1)
else:
    for i in range(0,len(str1)):
        if ord(str1[i])<=ord('9')and ord(str1[i])>=ord('0'):
            result+=str1[i]
        else:break
    m = eval(result)
    if m>pow(2,31)-1: result = pow(2,31)-1
    if m<pow(2,31)*(-1): result = pow(2,31)*(-1)
print(result)