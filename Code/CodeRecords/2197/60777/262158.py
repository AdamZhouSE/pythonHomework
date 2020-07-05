t=int(input())

for i in range(t):
    num=int(input())
    sur=[j for j in range(1,num+1)]
    sword=0
    while(len(sur)>1):
        if(sword+1>=len(sur)):
            del sur[0]
            sword=0
        else:
            del sur[(sword+1)]
            sword=(sword+1)%len(sur)
    print(sur[0])