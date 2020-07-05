T=int(input())
for i in range(0,T):
    s=list(input())
    lis=[]
    q=True
    for j in s:
        if(j=='[' or j=='(' or j=='{'):
            lis.append(j)
        else:
            if(len(lis)==0):
                q=False
                break
            if(j==']'):
                if(lis[len(lis)-1]=='['):
                    lis.pop(len(lis)-1)
                else:
                    q=False
                    break
            elif(j==')'):
                if(lis[len(lis)-1]=='('):
                    lis.pop(len(lis)-1)
                else:
                    q=False
                    break
            elif(j=='}'):
                if(lis[len(lis)-1]=='{'):
                    lis.pop(len(lis)-1)
                else:
                    q=False
                    break
        #print(lis)
    if(len(lis)!=0):
        q=False
    if(q==True):
        print("balanced")
    else:print("not balanced")