numlist=list(map(int,input("")[1:-1].split(",")))
numlist.sort()
for i in range(0,len(numlist),3):
    if(i==len(numlist)-1):
        print(numlist[i])
        break
    elif(numlist[i]!=numlist[i+1]):
        print(numlist[i])
        break