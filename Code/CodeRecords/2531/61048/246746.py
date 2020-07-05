def sort3():
    str=input()
    dic = {}
    for word in str:
        if word in dic.keys():
            dic[word]=dic[word]+1
        else:
            dic[word]=1
    for i in range(0, len(str) - 1):
        for j in range(0, len(str) - 1):
            if (dic[str[j]] < dic[str[j + 1]]):
                if (j == 0):
                    str = str[j + 1] + str[j] + str[j + 2:]
                elif j != len(str) - 2:
                    str = str[:(j)] + str[j + 1] + str[j] + str[j + 2:]
                else:
                    str = str[:j] + str[j + 1] + str[j]
    print(str)
    return


sort3()