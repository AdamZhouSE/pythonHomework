string=input()

dict={}         # 处理输入 放进map
tempArr=[]
tempStr=""
start=False
for c in string:
    if c=='[':
        start=True
    elif c==']':
        if tempStr!="":
            tempArr.append(tempStr)
            if dict.get(tempArr[0])==None:
                dict[tempArr[0]]=[tempArr[1]]
            else:    # 处理排序
                tempList=dict[tempArr[0]]
                tempList.append(tempArr[1])
                for i in range(len(tempList)-1):
                    str1=tempList[i]
                    str2=tempList[i+1]
                    for j in range(len(str1)):   #都是三个字母
                        if str1[j]<str2[j]:
                            break
                        elif str1[j]>str2[j]:
                            temp=tempList[i]
                            tempList[i]=tempList[i+1]
                            tempList[i+1]=temp
            tempArr=[]
            tempStr=""
        start=False
    else:
        if start:
            if c!=',':
                if c!='"' and c!=' ':
                    tempStr+=c
            else:
                tempArr.append(tempStr)
                tempStr=""

result=["JFK"]
while True:
    try:
        destination=dict[result[-1]][0]
        dict[result[-1]].pop(0)
        result.append(destination)
    except:
        break
print(result)

