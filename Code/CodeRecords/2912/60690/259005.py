str = input()
maxLen=0
for i in range(len(str)-1):
    thisMaxLen=1
    list = [str[i]]
    for j in range(i+1,len(str)):
        if str[j] not in list:
            list.append(str[j])
            thisMaxLen+=1
        else:
            break
    if maxLen<thisMaxLen:
        maxLen=thisMaxLen
print(maxLen)
