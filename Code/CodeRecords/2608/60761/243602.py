def substrPrint(string):
    vowel=[] #存放元音字母的索引
    consonant=[] #辅音字母的索引
    while string[0] not in ["a","e","i","o","u"]:
        string=string[1:]
    if len(string)<2:
        print("-1")
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
                        print(string[i:n]+string[k:j+1],end=" ") 
        print("")

n=int(input(""))
for i in range(n):
    a=input("")
    substrPrint(a)