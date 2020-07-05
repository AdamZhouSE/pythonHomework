str=input()
l=len(str)
i=0
boy=0
girl=0
while i<l:
    if(str[i]!="."):
        if(str[i]=='b'):
            if(i+2<l and str[i+1]=='o' and str[i+2]=='y'):
                i=i+3

            elif (i + 1 < l and str[i + 1] == 'o'):
                i = i + 2
            else:
                i+=1
            boy = boy + 1
        elif(str[i]=='o'):
            if (i + 1 < l and str[i + 1] == 'y' ):
                i = i + 2
            else:
                i+=1
            boy = boy + 1
        elif(str[i]=="y"):
            i+=1
            boy=boy+1
        elif (str[i] == 'g'):
            if (i + 3 < l and str[i + 1] == 'i' and str[i + 2] == 'r'and str[i + 3] == 'l'):
                i = i + 3
            if (i + 2 < l and str[i + 1] == 'i' and str[i + 2] == 'r'):
                i = i + 3
            elif (i + 1 < l and str[i + 1] == 'i'):
                i = i + 2
            else:
                i += 1
            girl=girl+1
        elif (str[i] == 'i'):
            if (i + 2 < l and str[i + 1] == 'r' and str[i + 2] == 'l'):
                i = i + 3
            elif (i + 1 < l and str[i + 1] == 'r'):
                i = i + 2
            else:
                i += 1
            girl = girl + 1
        elif (str[i] == 'r'):
            if (i + 1 < l and str[i + 1] == 'l'):
                i = i + 2
            else:
                i += 1
            girl = girl + 1
        elif(str[i]=='l'):
            i=i+1
            girl = girl + 1
    else:
        i=i+1
print(boy)
print(girl,end="")


