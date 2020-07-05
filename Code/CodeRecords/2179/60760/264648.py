firstline=input().split(" ")
length=int(firstline[0])      #字符串长度
numsofQue=int(firstline[1])   #问题数
str0=input()
abcds=[]
for i in range(numsofQue):
    abcds.append("".join(input().split(" ")))
results=[]   #存结果，也就是各个最长公共前缀的长度
def func(str1,str2):
    results=0
    for i in range(len(str1)):
        if str1[0:len(str1)-i]==str2[0:len(str1)-i]:
            results=len(str1)-i
    return results+1

for i in abcds:
    str1=str0[int(list(i)[0]):int(list(i)[1])]
    str2=str0[int(list(i)[2]):int(list(i)[3])]
    results.append(func(str1,str2))
for i in results:
    print(i)