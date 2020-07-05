def exam6():
    s=list(input())
    l=len(s)
    num=0
    for i in range(0,l):
        if s[i]== "Q":
            for j in range(i+1,l):
                if s[j]=="A":
                    for k in  range(j+1,l):
                        if s[k]=="Q":
                            num=num+1
    print(str(num))
exam6()