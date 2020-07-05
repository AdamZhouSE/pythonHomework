N,P=map(int,input().split());
list = input().split(" ");
Dict = {};
for key in list:
    if(len(key)==1):
        Dict[key] = ord(key[0])-ord('A');#8+11*32+14*322
    elif(len(key)==2):
        Dict[key] = (ord(key[0])-ord('A'))*32+ord(key[1])-ord('A');
    else:
        Dict[key] = (ord(key[len(key)-3]) - ord('A')) * 32*32 + (ord(key[(len(key)-2)]) - ord('A'))*32+ord(key[len(key)-1])- ord('A');
#print(Dict);
for key in Dict:
    Dict[key] = Dict[key]%P;

keyList = [];
valueList = [];
for key in  Dict:
    keyList.append(key);
for value in Dict.values():
        if value not in valueList:
            valueList.append(value);
        else:
            j=1;
            while(value in valueList):
                valuetmp = value;
                value=(value+j*j)%P;
                if(value not in valueList):
                    break;
                else:
                    value=valuetmp;
                    value = (value-j*j)%P;
                    if(value not in valueList):
                        break;
                value = valuetmp;
                j+=1;
            valueList.append(value);

res = "";
for ele in valueList:
    res=res+str(ele)+" ";

res = res[0:len(res)-1];
print(res);
