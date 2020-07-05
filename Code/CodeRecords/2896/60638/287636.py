inpu1=input().split(" ")
inpu2=input().split(" ")
string1=[]
string2=[]
for i in range(0,len(inpu1)):
    for j in range(0,len(inpu1[i])):
        string1.append(inpu1[i][j])
for i in range(0,len(inpu2)):
    for j in range(0,len(inpu2[i])):
        string2.append(inpu2[i][j])
find=True
for i in range(0,len(string2)):
    if string1.__contains__(string2[i]):
        string1.remove(string2[i])
    else:
        find=False
        break
if find:
    print("YES",end="")
else:
    print("NO",end="")