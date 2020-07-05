def Test():
    word=input()
    d=eval(input())
    d.sort()
    for i in range(0,len(d)):
        save=d[i]
        for j in range(0,len(d[i])):
            index=word.find(d[i][j])
            if(index!=-1):
                if(index==0):
                    d[i] = d[i][index + 1:]
                elif(index==len(d[i])-1):
                    d[i]=d[i][:index]
                else:
                    d[i]=d[i][:index]+d[i][index+1:]
        if(d[i]==""):
            print(save)
            break
    print()


if __name__ == "__main__":
    Test()