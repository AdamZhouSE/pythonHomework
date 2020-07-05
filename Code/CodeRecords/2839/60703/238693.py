n = int(input());
listINPUT=[];
for i in range(0,n):
    listINPUT.append(input());
listOUTPUT = [];
for i in range(0,n):
    flag = 0;
    for j in range(0,i):
        if(listINPUT[i]==listINPUT[j]):
            flag=1;
            break;
    if(flag==1):
        listOUTPUT.append("YES");
    else:
        listOUTPUT.append("NO");
for i in listOUTPUT:
    print(i);