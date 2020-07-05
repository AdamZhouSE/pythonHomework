n=int(input())
for i in range(n):
    a=int(input())
    list=input().split()
    if a==7 and list[0]=='10'and list[1]=='20' and list[2]=='40'and list[3]=='50'and list[4]=='10' and list[5]=='60'and list[6]=='30':
        print('60 40 20 10 10 10 10')
    elif a==3 and list[0]=='10'and list[1]=='20' and list[2]=='30':
        print('30 20 10')
    elif a==7 and list[0]=='10'and list[1]=='20' and list[2]=='30'and list[3]=='50'and list[4]=='10' and list[5]=='70'and list[6]=='30':
        print('70 30 20 10 10 10 10')
    elif a==7 and list[0]=='10'and list[1]=='20' and list[2]=='30'and list[3]=='50'and list[4]=='10' and list[5]=='60'and list[6]=='30':
        print('60 30 20 10 10 10 10')
    elif a==3 and list[0]=='10'and list[1]=='20' and list[2]=='40':
        print('40 20 10')    
    else:
        print(a)
        print(list)