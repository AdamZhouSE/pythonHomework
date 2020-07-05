str0 = input()
positionwithoutspace = 0
for i in range(len(str0)):
    if str0[i] != ' ':
        positionwithoutspace = i
        break
str1 = str0[positionwithoutspace:]
result = True
if str1[0]!="-" and str1[0]!="+" and (ord(str1[0])>ord('9')or ord(str1[0])<ord('0')):
    result = False
if result:
    position = 0
    for i in range(len(str1)-1,0,-1):
        if str0[i] != ' ':
            position = i
            break
    str2 = str1[0:position+1]
    for i in range(len(str2)):
        if str2[i] != "-" and str2[i] != "+" and (ord(str2[i]) > ord('9') or ord(str2[i]) < ord('0')) and str2[i]!='.':
            result = False
            break
    if str2[len(str2)-1] == 'e' or str2[len(str2)-1] == '.':result = False
    if result:
        if str2.find("e")!=-1:
            for i in range(str2.find("e")+1,len(str2)):
                if str2[i]==".":
                    result = False
                    break
print(result)
