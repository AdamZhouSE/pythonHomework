def exam2():
    str=list(input())
    s=[]
    string = [str[0]]
    for i in range(1,len(str)):
        if string.count(str[i])==0:
            string.append(str[i])
        else:
            s.append(''.join(string))
            string.clear()
            string.append(str[i])
    s.sort(key=lambda i:len(i),reverse=True)
    print(len(s[0]))
exam2()