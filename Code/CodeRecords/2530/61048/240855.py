def sort2():
    str1=input()
    str2=input()
    dic={}
    a=0
    for word in str1:
        a=a+1
        dic[word]=a

    for num in range(0,len(str2)):
        if str2[num] in dic.keys():
            continue
        else:
            dic[str2[num]]=0

    for i in range(0,len(str2)-1):
        for j in range(0,len(str2)-1):
            if(dic[str2[j]]>dic[str2[j+1]]):
                if(j==0):
                    str2 =str2[j + 1] + str2[j] + str2[j + 2:]
                elif j!=len(str2)-2:
                    str2 = str2[:(j)] + str2[j + 1] + str2[j] + str2[j + 2:]
                else:
                    str2=str2[:j]+str2[j+1]+str2[j]
    print(str2)
    return str2
sort2()