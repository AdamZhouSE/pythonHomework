import re
def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def satisfyFunc(list):
    i=0;
    while(i<len(list)):
        j=i+1;
        while(j<len(list)):
            x=0;
            while(x<len(list)):
                if(x==i or x==j):
                    x+=1;
                    continue;
                y=x+1;
                while(y<len(list)):
                    if(y==j and y==i):
                        y+=1;
                        continue;
                    if(list[y]+list[x]==list[j]+list[i]):
                        print(i,end=" ");
                        print(j, end=" ");
                        print(x, end=" ");
                        print(y);
                        return;
                    y+=1;
                x+=1;
            j+=1;
        i+=1;
    print("no pairs");


Total=int(input());
i=0;
while(i<Total):
    S=input();
    list=input();
    temp="";
    j=0;
    ans=[];
    while(j<len(list)):
        if(list[j]>='0' and list[j]<='9'):
            temp+=list[j];
        else:
            if(temp!=''):
                ans.append(temp);
            temp="";
        j+=1;
    if(temp!=""):
        ans.append(temp);
    satisfyFunc(makeIntList(ans));
    i+=1;