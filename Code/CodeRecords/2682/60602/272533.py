def resetNum(string,L,R):
    i=L;
    while(i<=R):
        if(string[len(string)-i]=="0" and i!=1):
            string=string[0:len(string)-i]+"1"+string[len(string)-i+1:]
        elif(string[len(string)-i]=="0" and i==1):
            string = string[0:len(string) - i] + "1";
        i+=1;
    return string;

Total=int(input());
i=0;
while(i<Total):
    temp=input().split(" ");
    string=temp[0];
    L=int(temp[1]);
    R=int(temp[2]);
    ans=resetNum(bin(int(string)),L,R);
    ans=int(ans,2);
    print(ans);
    i+=1;
