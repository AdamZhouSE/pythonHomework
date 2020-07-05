def judge(c):

    top=0
    i=0;
    count=0
    while(count!=len(c)):

        if(c[i]=='('):top+=1;
        if(c[i]==')'):

         if(top>0):top-=1;
         else: return False;

        i+=1;
        count+=1

    if(top!=0):return False;
    else: return True;







string=input()
if(judge(string)):
    print("YES",end="")
else:
    print("NO",end="")