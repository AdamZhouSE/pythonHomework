def input_manage():
    temp=input()
    temp=temp[2:len(temp)-2]
    array=temp.split('","')
    table=[['' for _ in range(3)] for _ in range(len(array))]
    for i in range(len(array)):
        table[i][0]=array[i][0]
        table[i][1]=array[i][1:3]
        table[i][2]=array[i][3]
    return table
def judge(table):
    list=[[0 for _ in range(26)]for _ in range(26)]
    for i in range(len(table)):
        num1=ord(table[i][0])-97
        num2=ord(table[i][2])-97
        if table[i][0]==table[i][2]:
            if table[i][1]=="!=":
                return False
        if list[num1][num2]==0:
            if table[i][1]=="==":
                list[num1][num2]=1
            else:
                list[num1][num2]=-1
        else:
            if table[i][1]=="==":
                if list[num1][num2]!=1:
                    return False
            else:
                if list[num1][num2]!=-1:
                    return False
    return True
table=input_manage()
if judge(table):
    print("true")
else:
    print("false")