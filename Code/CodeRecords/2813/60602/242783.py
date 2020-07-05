def cardGame(Namelist,Scorelist):
    dict={};
    for element in Namelist:
        dict[element]=0;
    i=0;
    while(i<len(Scorelist)):
        dict[Namelist[i]]+=Scorelist[i];
        i+=1;
    MAX=0;
    winner=[];
    for element in dict:
        if(dict[element]>MAX):
            MAX=dict[element];
    for element in Namelist:
        dict[element]=0;
    i=0;
    while(i<len(Scorelist)):
        dict[Namelist[i]]+=Scorelist[i];
        if(dict[Namelist[i]]>=MAX):
            print(Namelist[i]);
            return;
        i+=1;





Total=int(input());
i=0;
Namelist=[];
Scorelist=[];
while(i<Total):
    list=str(input());
    list=list.split(" ");
    Namelist.append(list[0]);
    Scorelist.append(int(list[1]));
    i+=1;
cardGame(Namelist,Scorelist);