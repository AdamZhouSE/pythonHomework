Neq=int(input())
for i in range(0,Neq):
    l=int(input())
    List=input().split(" ")
    ZERO=0
    x=0
    while(x!=len(List)):
        if(List[x]=='0'):
            ZERO=ZERO+1
            List.pop(x)
            x=x-1
        x=x+1
    for item in List:
        print(item,end=" ")
    for x in range(0,ZERO):
            print("0",end=" ")
    print("")