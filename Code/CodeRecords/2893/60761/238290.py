numlist=list(map(int,input("")[1:-1].split(",")))
for i in range(0,len(numlist),3):
    if(numlist[i]!=numlist[i+2]):
        print(numlist[i])
        break