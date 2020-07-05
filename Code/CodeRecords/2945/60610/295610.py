string=input();
boy=0;
girl=0;
for i in range(len(string)-4):

    if(string[i]=="b") | (string[i+1]=="o") |(string[i+2]=="y"):
       boy+=1;
    if (string[i] == "g") | (string[i + 1] == "i") | (string[i + 2] == "r")|(string[i+3]=="l"):
        girl += 1;
print(boy)
print(girl,end="")