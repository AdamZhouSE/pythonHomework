def strop2():
    string=input().split(' ')
    str1=''
    str2=''
    for word in string[0]:
        if(word!=' '):
            str1=str1+word


    for word in string[len(string)-1]:
        if(word!=' '):
            str2=str2+word

    res=0
    if(len(str1)>len(str2)):
        slen=len(str2)
    else:
        slen=len(str1)
    for i in range(0,slen):
        if(str1[i]==str2[i]):
            continue
        else:
            res=ord(str1[i])-ord(str2[i])
            break
    print(res)
    return

strop2()


