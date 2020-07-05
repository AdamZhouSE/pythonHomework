'''
分别变一个数字，转换为十进制看是不是相等
外面循环是三进制数
里面循环二进制数
唯一性不会证
'''
Str1=input();
Str2=input();
int2=int(Str2,3);
tempInt2=0;
ZERO_ONE=[0,1];
ONE_TWO=[1,2];
ZERO_TWO=[0,2];
for i in range(0,len(Str2)):
    tempStr2=Str2;
    if(Str2[i]=='0'):
        for j in ONE_TWO:
            tempStr2 = Str2[0:i]+str(j)+Str2[i+1:len(Str2)];
            tempInt2=int(tempStr2,3);
            for m in range(0,len(Str1)):
                tempStr1=Str1;
                if(tempStr1[m]=='1'):
                    tempStr1=Str1[0: m] + '0' + Str1[m + 1: len(Str1) ];
                else:
                    tempStr1=Str1[0: m] + '1' + Str1[m + 1: len(Str1) ];

                tempInt1=int(tempStr1,2);
                if(tempInt2==tempInt1):
                    print(tempInt1,end="");
    elif(Str2[i]=='1'):
        for j in ZERO_TWO:
            tempStr2 = Str2[0:i] + str(j) + Str2[i + 1:len(Str2)];
            tempInt2 = int(tempStr2, 3);
            for m in range(0, len(Str1)):
                tempStr1 = Str1;
                if (tempStr1[m] == '1'):
                    tempStr1 = Str1[0: m] + '0' + Str1[m + 1: len(Str1)];
                else:
                    tempStr1 = Str1[0: m] + '1' + Str1[m + 1: len(Str1)];

                tempInt1 = int(tempStr1, 2);
                if (tempInt2 == tempInt1):
                    print(tempInt1,end="");
    else:
        for j in ZERO_ONE:
            tempStr2 = Str2[0:i] + str(j) + Str2[i + 1:len(Str2)];
            tempInt2 = int(tempStr2, 3);
            for m in range(0, len(Str1)):
                tempStr1 = Str1;
                if (tempStr1[m] == '1'):
                    tempStr1 = Str1[0: m] + '0' + Str1[m + 1: len(Str1)];
                else:
                    tempStr1 = Str1[0: m] + '1' + Str1[m + 1: len(Str1)];

                tempInt1 = int(tempStr1, 2);
                if (tempInt2 == tempInt1):
                    print(tempInt1,end="");