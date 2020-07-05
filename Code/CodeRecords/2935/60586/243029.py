def exam6():
    s=list(input())
    l=len(s)
    num=0
    for i in s:
        if i== "Q":
            for j in range(i+1,l):
                if j=="A":
                    for k in  range(j+1,l):
                        if k=="Q":
                            num=num+1
    print(str(num))
exam6()