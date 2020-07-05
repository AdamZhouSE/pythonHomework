ins=int(input());
result="";
for i in range(ins):
    string=input();
    if(string[0]=="T"):
        result=result+string[2];
    elif(string[0]=="U"):
        result=result.replace(result[-int(string[2]):],"",1);
    else:
        print(result[int(string[2])-1])