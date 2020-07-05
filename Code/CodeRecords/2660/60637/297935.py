instrction_nums=(int)(input())
instrctions=[]
string=""
for i in range(instrction_nums):
    instrctions.append(input().split(' '))
for i in instrctions:
    if(i[0]=='T'):
        string+=i[1]
    elif(i[0]=='U'):
        string=string[:-(int)(i[1])]
    elif(i[0]=='Q'):
        print(string[(int)(i[1])-1])
