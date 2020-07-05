import re;
listENG=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
m,n=map(int,input().split())
Str1=input();
Str2=input();
indexOfStar1 = Str1.find('*');
indexOfStar2 = Str2.find('*');
num=0;
listOfIndex = [];
pattern  =(Str1[0:indexOfStar1]+'[a-z]'+Str1[indexOfStar1+1:]);
for i in range(0,len(Str2)-len(Str1)+2):
    flag=0;
    for ENG in listENG:
        ppp =Str2[i:i+len(Str1)];
        if("*" in ppp):
            ppp=ppp[0:ppp.find("*")]+ENG+ppp[ppp.find("*")+1:]
        list = re.findall(pattern,ppp);
        for ele in list:
            if (ele != ''):
                num += 1;
                listOfIndex.append(i);
                flag=1;
                break;
        if(flag==1):
            break;
print(num);
for i in range(0,len(listOfIndex)-1):
    print(listOfIndex[i]+1,end=" ");
print(listOfIndex[len(listOfIndex)-1]+1,end=" ");
print();