num=int(input());
for i in range(num):
    string=input().split();
    binString=bin(int(string[0]))[2:];
    L=int(string[1]);
    R=int(string[2]);
    for i in range(len(binString)-R,len(binString)-L+1):
        if(binString[i]=="0"):
            binString=binString[:i]+"1"+binString[i+1:];
        else:
            binString = binString[:i] + "0" + binString[i + 1:];
    print(int(binString,2));