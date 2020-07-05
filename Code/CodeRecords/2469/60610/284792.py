num=int(input());
for i in range(num):
    string=input();
    cout=0;
    count=0;
    for k in range(1,len(string)):
        for j in range(len(string)-k+1):
            result=string[j:j+k];
            for l in string:
                if(l in result):
                    cout+=1;
                else:
                    break;
            if(cout==len(string)):
                count=1;
                break;
            cout=0;
        if(count==1):
            break;
    print(k)