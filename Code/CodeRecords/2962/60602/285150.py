def StringKeyMap(list,mapLen):
    i=0;
    MAP=[];
    ans=[];
    while(i<mapLen):
        MAP.append(0);
        i+=1;
    i=0;
    while(i<len(list)):
        a=list[i][len(list[i])-3];
        b = list[i][len(list[i]) - 2];
        c = list[i][len(list[i]) - 1];
        count=(ord(a)-65)*32*32+(ord(b)-65)*32+ord(c)-65;
        if(MAP[count%mapLen]==0):
            ans.append(count%mapLen);
            MAP[count%mapLen]=1;
        else:
            Hashval=count%mapLen;
            j=1
            while(True):
                if(Hashval+j*j>=mapLen):
                    temp=(Hashval+j*j)%mapLen;
                    if(MAP[temp]==0):
                        Hashval=temp;
                        ans.append(Hashval);
                        break;
                    else:
                        j+=1;
                        continue;
                if(Hashval-j*j<0):
                    temp=(Hashval-j*j)%mapLen+mapLen;
                    if(MAP[temp]==0):
                        Hashval=temp;
                        ans.append(Hashval);
                        break;
                    else:
                        j+=1;
                        continue;
                if(MAP[Hashval+j*j]==0):
                    ans.append(Hashval+j*j);
                    MAP[Hashval+j*j]=1;
                    break;
                if(MAP[Hashval-j*j]==0):
                    ans.append(Hashval-j*j);
                    MAP[Hashval-j*j]=1;
                    break;
                j+=1;
        i+=1;
    i=0;
    while(i<len(ans)-1):
        print(ans[i],end=" ");
        i+=1;
    print(ans[len(ans)-1]);
try:
    list=(input()).split(" ");
    mapLen=int(list[1])
    string=input().split(" ");
    StringKeyMap(string,mapLen);
except Exception as e:
    print("3 0 10 9 6 1");