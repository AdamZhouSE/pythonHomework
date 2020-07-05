t=int(input())
for i in range(t):
    string_1=list(input())
    string_2=list(input())
    all_1=[]
    all_2=[]
    alls=[]
    for i in string_1:
        if(not i in all_1):
            all_1.append(i)
        if(not i in alls):
            alls.append(i)
    for i in string_2:
        if(not i in all_2):
            all_2.append(i)
        if(not i in alls):
            alls.append(i)
    ans=""
    for i in alls:
        if((not i in all_1)|(not i in all_2)):
            ans=ans+i
    print(ans)
            
    