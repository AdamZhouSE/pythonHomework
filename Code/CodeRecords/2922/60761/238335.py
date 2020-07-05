n=int(input(""))
numlist=list(map(int,input("").split(" ")))
numset=set(numlist)
if len(numset)>3:
    print("NO")
elif len(numset)<3:
    print("YES")
else:
    numlist=list(numset)
    numlist.sort()    
    if numlist[0]+numlist[2]==2*numlist[1]:
        print("YES")
    else:
        print("NO")
        print(numlist)