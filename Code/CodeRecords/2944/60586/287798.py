def exam11():
    exp=list(input())
    numOfZ=0
    i=0
    while(True):
        if(exp[i]=='('):
            numOfZ+=1
        if(exp[i]==")"):
            numOfZ-=1
        if(exp[i]=="@"):
            break
        i+=1
    if(numOfZ==0):
        print("YES",end="")
    else:
        print("NO",end="")
exam11()        