string="1379";
num=input();
if(num[-1] in string):
    string="1";
    num=int(num);
    while(True):
        if(int(string)%num==0):
            print(len(string));
            break;
        string+="1";
else:
    print(-1);