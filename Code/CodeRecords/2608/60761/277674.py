def substrPrint(string):
    vowel=[] #存放元音字母的索引
    consonant=[] #辅音字母的索引
    result=[]
    while string[0] not in ["a","e","i","o","u"]:
        string=string[1:]
    if len(string)<2:
        return [-1]
    else:
        for i in range(len(string)):
            if string[i] in ["a","e","i","o","u"]:
                vowel.append(i)
            else:
                consonant.append(i)
        for i in vowel:
            for j in consonant:
                for n in range(i+1,j+1):
                    for k in range(n,j+1):
                        result.append(string[i]+string[n:k]+string[j])
                        result.append(string[i:n]+string[k:j+1])
        result=list(set(result))
        result.sort()
        return result                 

n=int(input(""))
for i in range(n):
    a=input("")
    result=substrPrint(a)
    for substr in result:
        if(substr==result[-1]):
            print(substr)
        else:
            print(substr,end=" ")