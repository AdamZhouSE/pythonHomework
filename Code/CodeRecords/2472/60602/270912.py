def specialChar(string):
    i=0
    judge=True
    ans=""
    while(i<len(string)):
        j=0
        while(j<len(string)):
            if(j!=i):
                if(string[j]==string[i]):
                    judge=False
            j+=1
        if(judge):
            ans+=string[i]
            break
        judge=True
        i+=1
    if(ans!=""):
        print(ans)
    else:
        print(-1)

Total=int(input())
i=0
while(i<Total):
    N=int(input())
    string=input()
    specialChar(string)
    i+=1