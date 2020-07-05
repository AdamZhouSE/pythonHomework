def checkin(substr:list,parstr:str):
    check = True
    for t in range(len(parstr)):
        if parstr[t] in substr:
            substr.remove(parstr[t])
        else:
            break
    return check

ucnum = int(input())
ans = list()
for i in range(ucnum):
    str1 = input()
    str2 = input()
    anstr = str()
#    lens = len(str1)
    for j in range(len(str2),len(str1)+1):#length of substring
        for k in range(len(str1)-j):#start of substring
            tempstr = str1[k:k+j]
            templist = list(tempstr)
            if checkin(templist,str2):
                ans.append(tempstr)
                break
        if len(ans)==i+1:
            break
    ans.append(anstr)
for i in ans:
    print(i)
