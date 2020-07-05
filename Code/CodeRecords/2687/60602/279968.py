def binaryToInteger(string):
    i=len(string)-1;
    ans=0;
    j=0;
    while(i>=0):
        ans+=pow(2,j)*int(string[i]);
        i-=1;
        j+=1;
    return ans;
def binexchangeNum(n):
    bin=0;
    string = "1";
    ans=[];
    while(True):
        if(binaryToInteger(string)<=n):
            ans.append(binaryToInteger(string));
        else:
            break;
        if(bin%2==0):
            string+="0";
        else:
            string+="1";
        bin+=1;
    i=0;
    while(i<len(ans)-1):
        print(ans[i],end=" ");
        i+=1;
    print(ans[len(ans)-1]);
Total=int(input());
i=0;
while(i<Total):
    n=int(input());
    binexchangeNum(n);
    i+=1;