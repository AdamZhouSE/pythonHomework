def exam2():
    str=list(input())
    s=[]
    string = str[0]
    for i in range(1,len(str)):
        if str[i-1]!=str[i-1]:
            string=string+str[i]
        else:
            s.append(string)
            string=str[i]
    s.sort(key=lambda i:len(i),reverse=True)
    print(len(s[0]))
exam2()