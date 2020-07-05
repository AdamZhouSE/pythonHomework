import operator
str1=input()
str2=input()

def findSubStr(string):
    res=[]
    for i in range(0,len(string)):
        for j in range(i+1,len(string)+1):
            res.append(string[i:j])
    return res

subStrs1=findSubStr(str1)
subStrs2=findSubStr(str2)

result=0
for subStr1 in subStrs1:
    result=result+subStrs2.count(subStr1)

print(result,end="")