string=input();
count=0;
for i in range(len(string)):
    b= string[i:]+string[0:i];
    if(b[0]!="0"):
        a=int(b);
        Estring=bin(a).replace("0b","");
        if "1" not in Estring[1:]:
            print("true");
            count=1;
            break;
if(count==0):
    print("false");