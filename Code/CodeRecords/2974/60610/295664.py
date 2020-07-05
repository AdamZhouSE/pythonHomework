
num=int(input());
string=input();

output=0;
for i in range(1,num-1):
    string1=string[:i];
    string2=string[i:];
    A = 0;
    B = 0;
    midA=[];
    midB=[];
    for j in range(len(string1)):
        for k in range(len(string1)-j):
            string3=string1[k:k+j+1];
            if(string3 not in midA ):
                midA.append(string3);
                if(len(string3)%2!=0):
                    result=string3[::-1];
                    if(result==string3):
                        A+=1;
    for j in range(len(string2)):
        for k in range(len(string2)-j):
            string3 = string2[k: k + j+1];
            if (string3 not in midB):
                midB.append(string3);
                if (len(string3) % 2 != 0):
                    result = string3[::-1];
                    if (result != string3):
                       B+=1;
                else:
                    B+=1;
        if(A*B>output):
            output=A*B;

print(output)