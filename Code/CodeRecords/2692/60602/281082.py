def abilityToTrans(list,D):
    list.append(list[len(list)-1]+1);
    weight=max(list);
    judge=True;
    while(judge):
        temp=weight;
        count = 0;
        i=0;
        while(True):
            weight=temp;
            while(weight>0):
                if(weight-list[i]>=0):
                    weight-=list[i];
                else:
                    break;
                i+=1;
                if(i<len(list)):
                    continue;
                else:
                    break;
            count+=1;
            if(count>D):
                temp+=1;
                weight=temp;
                judge=True;
                break;
            if(count<=D and i==len(list)-1):
                judge=False;
                break;
    print(temp);

list=eval(input());
D=int(input());
abilityToTrans(list,D);