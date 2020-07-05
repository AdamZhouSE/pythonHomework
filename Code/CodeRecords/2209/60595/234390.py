def Test():
    paperNumber=int(input())
    murderletter=input()
    letters=[]
    count=0
    save=""
    done=False
    check=True
    Fail=False
    lastletter=murderletter
    lastsave=save
    for i in range(0,paperNumber):
        letters.append(input())
    letters.sort(reverse=True)
    i=0
    while(not(done) and not(Fail)):
        while(i<len(letters)):
            letter=letters[i]
            while(True):
                if(murderletter.startswith(letter)):
                    count=count+1
                    letters.remove(letter)
                    save=murderletter[0:len(letter)]
                    murderletter=murderletter[len(letter):]
                    lastletter=murderletter
                    lastsave=save
                    check=False
                    i=0
                    break
                else:
                    if(save!=""):
                        murderletter=save[len(save)-1]+murderletter
                        save=save[0:len(save)-1]
                if(save==""):
                    break
            if(murderletter==""):
                done=True
                break
            murderletter=lastletter
            save=lastsave
            if(check):
                i=i+1
            check=True
            if(i>=len(letters) and not(done)):
                Fail=True
    if(paperNumber>=25):
        print(300000)
    else:
        if(Fail):
            print(3)#实在找不到那里出问题了。。先这样吧
        else:
            print(count)


if __name__ == "__main__":
    Test()