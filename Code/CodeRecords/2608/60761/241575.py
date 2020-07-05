def substrPrint(string):
    vowel=[] #存放元音字母的索引
    consonant=[] #辅音字母的索引
    if string[0] not in ["a","e","i","o","u"]:
        string=string[1:]
    if len(string)<=2:
        print("-1")
    else:
        for i in range(len(string)):
            if string(i) in ["a","e","i","o","u"]:
                vowel.append(i)
            else:
                consonant.append(i)
        for i in vowel:
            for j in consonant:
                for n in range(i+1,j):
                    for k in range(n,j):
                        print(string[i:n]+string[k:j])
    return 0                    

n=int(input(""))
for i in range(n):
    a=input("")
    print(a)
    substrPrint(a)
    