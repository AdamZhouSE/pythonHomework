def Test():
    word=input()
    d=eval(input())
    d.sort()
    result=""
    for i in range(0,len(d)):
        save=d[i]
        while(len(d[i])!=0):
            index=word.find(d[i][0])
            if(index!=-1):
                d[i]=d[i][1:]
            else:
                break
        if(d[i]==""):
            result=save if len(save)>=len(result) else result
    print(result)


if __name__ == "__main__":
    Test()