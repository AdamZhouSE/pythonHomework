str = input()
str = str.replace("[",'')
str = str.replace("]",'')
strList = str.split(',')
res = 0
strList.sort(reverse=True);
for i in range(len(strList)-2):
    if int(strList[i]) < int(strList[i+1]) + int(strList[i+2]):
        res = int(strList[i]) + int(strList[i+1]) + int(strList[i+2])
        break
print(res)
