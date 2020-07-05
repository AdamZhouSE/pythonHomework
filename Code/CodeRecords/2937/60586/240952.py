def exam3():
    ex=list("CODEFESTIVAL2016")
    str=list(input())
    sett=set(ex)
    l=len(sett)
    for item in str:
        sett.add(item)
    print(len(sett)-l)
exam3()