num=int(input());
for i in range(num):
    string=input();
    result=[];

    for i in string:
        if (i=="[") | (i=="{") | (i=="("):
            result.append(i);
        if(len(result)==0)&((i=="]") | (i=="}") | (i==")")):
            result.append(-1);
            break;
        elif(i=="]"):
            if(result[-1]=="["):
                del result[-1];
            else:
                print("nit balanced");
                break;
        elif (i == "}"):
            if (result[-1] == "{"):
                del result[-1];
            else:
                print("nit balanced");
                break;
        elif (i == ")"):
            if (result[-1] == "("):
                del result[-1];
            else:
                print("nit balanced");
                break;
    if(len(result)==0):
        print("balanced");
    else:
        print("not balanced");