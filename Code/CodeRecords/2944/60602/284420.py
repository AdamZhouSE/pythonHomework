def expressionMatch(string):
    i=0;
    count=0;
    while(i<len(string)):
        if(string[i]=='('):
            count+=1;
        if(string[i]==')'):
            count-=1;
        if(count<0):
            break;
        i+=1;
    if(count==0):
        print("YES",end="");
    else:
        print("NO",end="");

string=input();
expressionMatch(string);