def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1

    return lcm


def hcf(x, y):
    """该函数返回两个数的最大公约数"""
    HCF=1;
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            HCF = i

    return HCF
def fractionCalcu(string):
    if(string[0]!='-'):
        string='+'+string;
    i=0;
    listChild=[];
    listM=[];
    listSign=[];
    while(i<len(string)):
        if(string[i]=='/'):
            listChild.append(int(string[i-1]));
            listM.append(int(string[i+1]));
            listSign.append(string[i-2]);
        i+=1;
    LCM=1;
    i=0;
    while(i<len(listM)):
        LCM=lcm(LCM,listM[i]);
        i+=1;
    i=0;
    while(i<len(listChild)):
        listChild[i]=int(listChild[i]*(LCM/listM[i]));
        i+=1;
    sum=0;
    i=0;
    while(i<len(listChild)):
        sum+=int(listSign[i]+str(listChild[i]));
        i+=1;
    temp=hcf(sum,LCM);
    sum=int(sum/temp);
    LCM=int(LCM/temp);
    print(sum,end="");
    print('/',end="");
    if(sum!=0):
        print(LCM);
    else:
        print(1);

string=str(input());
fractionCalcu(string);