def longestCommonPrefix(a,str2):
    result=[]
    s2 = str2
    for temp in a:
        s1 = temp
        same=0
        for i, j in enumerate(s1):
            if i>=len(s2) or not j==s2[i]:
                break
            if j == s2[i]:
                same=same+1
        result.append(same)
    return max(result)


def getcut(Str):

    a = []
    MaxLength = len(Str)
    for length in range(0, MaxLength):
        for i in range(0, MaxLength - length):
            a.append(Str[i:i + length+1])
    a=list(set(a))
    return a
temp=input()
length=int(temp[0])
NumberOfQues=int(temp[2])
s=input()
result=[]
inputstr=[""]*NumberOfQues
for i in range(0,NumberOfQues):
    inputstr[i]=input()

for i in range(0,NumberOfQues):
    temp=inputstr[i]
    a=int(temp[0])
    b=int(temp[2])
    c=int(temp[4])
    d=int(temp[6])
    str1=s[a-1:b]
    str2=s[c-1:d]
    a=[]
    a=getcut(str1)

    print( longestCommonPrefix(a,str2))
