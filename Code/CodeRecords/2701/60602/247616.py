def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def setChess(table,list,round):
    if(round%2==0):
        table[list[0]][list[1]]='X';
    else:
        table[list[0]][list[1]]='O';
    return table;

def checkTable(table):
    if(table[0][0]==table[0][1]and table[0][1]==table[0][2]and table[0][0]!=' '):
        if(table[0][0]=='X'):
            print("A");
            return
        else:
            print("B");
            return
    if(table[1][0]==table[1][1]and table[1][1]==table[1][2]and table[1][0]!=' '):
        if(table[1][0]=='X'):
            print("A");
            return
        else:
            print("B");
            return
    if(table[2][0]==table[2][1]and table[2][1]==table[2][2]and table[2][0]!=' '):
        if(table[2][0]=='X'):
            print("A");
            return
        else:
            print("B");
            return
    if(table[0][0]==table[1][0]and table[1][0]==table[2][0]and table[0][0]!=' '):
        if(table[0][0]=='X'):
            print("A");
            return
        else:
            print("B");
            return
    if(table[0][1]==table[1][1]and table[1][1]==table[2][1]and table[0][1]!=' '):
        if(table[0][1]=='X'):
            print("A");
            return
        else:
            print("B");
            return
    if(table[0][2]==table[1][2]and table[1][2]==table[2][2]and table[0][2]!=' '):
        if(table[0][2]=='X'):
            print("A");
            return
        else:
            print("B");
            return
    if(table[0][0]==table[1][1]and table[1][1]==table[2][2]and table[0][0]!=' '):
        if(table[0][0]=='X'):
            print("A");
            return
        else:
            print("B");
            return
    if(table[0][2]==table[1][1]and table[1][1]==table[2][0]and table[0][2]!=' '):
        if(table[0][2]=='X'):
            print("A");
            return
        else:
            print("B");
            return

    i=0;
    j=0;
    IsDraw=True;
    while(i<len(table)):
        while(j<len(table[0])):
            if(table[i][j]==' '):
                IsDraw=False;
            j+=1;
        i+=1;
    if(IsDraw):
        print("Draw");
        return
    else:
        print("Pending");
        return
def ticktaktoe(list):
    table=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']];
    i=0;
    while(i<len(list)):
        table=setChess(table,list[i],i);
        i+=1;
    checkTable(table);


list=[];
temp=str(input());
i=0;
ans=[];
while(i<len(temp)):
    if(temp[i]>='0' and temp[i]<='9'):
        list.append(temp[i]);
    i+=1;
i=0;
while(i<len(list)):
    temp=[];
    temp.append(list[i]);
    temp.append(list[i+1]);
    temp=makeIntList(temp);
    ans.append(temp);
    i+=2;

ticktaktoe(ans);