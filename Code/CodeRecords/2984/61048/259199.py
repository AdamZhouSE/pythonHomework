def strop4():
    str1=input()
    str2=input()
    caseno=0
    if(len(str1)!=len(str2)):
        caseno=1
    else:
        issame=True
        for i in range(0,len(str1)):
            if(str1[i]!=str2[i]):
                issame=False
        if(issame):
            caseno=2
        else:
            isuppersame=True
            str1_upper=str1.upper()
            str2_upper=str2.upper()
            for i in range(0, len(str1_upper)):
                if (str1_upper[i] != str2_upper[i]):
                    isuppersame = False
            if(isuppersame):
                caseno=3
            else:caseno=4
    print(caseno)
    return

strop4()