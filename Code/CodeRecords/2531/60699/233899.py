def takeSecond(elem):
    return elem[1]

dict={}
str=input()
for i in str[0:]:
    if i not in dict:
        dict[i]=1
    else:
        dict[i]=dict[i]+1;
strs=[]
for i in dict:
    temp=[i,dict[i]]
    strs.append(temp)

strs.sort(key=takeSecond,reverse=True)

res=""
for i in strs:
    res+=(i[0]*i[1])
print(res)
