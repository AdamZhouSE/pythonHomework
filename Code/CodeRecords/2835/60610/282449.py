def alog(alo,result):
    output = 0;
    string = str(int(alo) * 90);
    while (len(str(string)) <= len(result)):
        string = str(int(alo) * 90);
        len0 = string.count("0");
        len5 = string.count("5");
        if ((len0 <= result.count("0")) & (len5 <= result.count("5"))):
            if (int(string) > output):
                output = int(string);
        alo = alo + "0";
    return output;

num=int(input());
string=input().split();
result=sorted(string,reverse=True);
mid=int("".join(result));
output=0;
alo=str(61728395);
a=alo;
while(len(alo)<=len(result)):
    comp=alog(alo,result);
    if(comp>output):
        output=comp;
    alo=alo+"0"+a;
if(output==0):
    if("0" in result):
        print(0);
    else:
        print(-1);
elif(output>0):
    print(output);
