def exam3():
    ex=list("CODEFESTIVAL2016")
    str=list(input())
    num=0
    for i in range(len(str)):
        if str[i]!=ex[i]:
            num=num+1
    print(num)
exam3()