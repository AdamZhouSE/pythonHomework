string=input();
words=eval(string);
mid=[];
if(words[0][1:3]=="=="):
    mid.append([words[0][0],words[0][3]])
cout=0;
for i in words:
    if(i[1:3]=="=="):
        count=-1;
        for j in range(len(mid)):
            if(i[0] in mid[j])&(count!=-1):
                cout=1;
                break;
            elif(i[3] in mid[j])&(count!=-1):
                cout=1;
                break;
            elif(i[0] in mid[j])|(i[3] in mid[j]):
                count=j;

        if(cout==1):
            break;
        if(count==-1):
            mid.append([i[0],i[3]]);
        else:
            if(i[0] not in mid[count]):
                mid[count].append(i[0])
            elif(i[3] not in mid[count]):
                mid[count].append(i[3])
    else:
        for j in range(len(mid)):
            if(i[0] in mid[j])&(i[3] in mid[j]):
                cout=1;
                break;
            else:
                if (i[0] in mid[j])&(cout==0):
                    cout=2;
                elif(i[3] in mid[j])&(cout==0):
                    cout=3;
                elif((i[3] in mid[j])&(cout!=0))|((i[0] in mid[j])&(cout!=0)):
                    cout=4;
        if(cout==1):
            break;
        else:
            if(cout==2):
                mid.append([i[3]])
            elif(cout==3):
                mid.append([i[0]]);
            elif(cout==4):
                mid.append([i[0]]);
                mid.append([i[3]]);
            cout=0;

if(cout==1):
    print("false");
else:
    print("true");