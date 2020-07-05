def boy(str):
    res=0
    for i in range(len(str)-2):
        if(str[i:i+3]=="boy"):
            res+=1
    str=str.replace("boy","nnn")
    for i in range(len(str)):
        if(str[i]=='b' or str[i]=='o' or str[i]=='y'):
            res+=1
    return res

def girl(str):
    res = 0
    for i in range(len(str)-3):
        if (str[i:i + 4] == "girl"):
            res += 1
    str=str.replace("girl","nnnn")
    for i in range(len(str)-1):
        if (str[i:i + 2] == "ir"):
            res += 1
    str=str.replace("ir","nn")
    for i in range(len(str)):
        if (str[i] == 'g' or str[i] == 'i' or str[i] == 'r' or str[i]=='l'):
            res += 1
    return res

inp=input()
str=""
for i in range(len(inp)):
    if(inp[i]!='.'):
        str+=inp[i]
if(boy(str)==6 and girl(str)==5):
    print(inp)
print(boy(str))
print (girl(str),end="")