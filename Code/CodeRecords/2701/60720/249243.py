list1=eval(input())
list2=[[0 for i in range(3)]for i in range(3)]
isF=True
for i in range(len(list1)):
    if i%2==0:
        list2[list1[i][0]][list1[i][1]]=1
    else:
        list2[list1[i][0]][list1[i][1]]=2
for i in range(3):
    if list2[i][0]==list2[i][1]==list2[i][2]==1 or list2[0][i]==list2[1][i]==list2[2][i]==1:
        print('A')
        isF=False
        break
    if list2[i][0]==list2[i][1]==list2[i][2]==2 or list2[0][i]==list2[1][i]==list2[2][i]==2:
        print('B')
        isF=False
        break
if isF:
    if list2[0][0]==list2[1][1]==list2[2][2]==1 or list2[0][2]==list2[1][1]==list2[2][0]==1:
        print('A')
    elif list2[0][0]==list2[1][1]==list2[2][2]==2 or list2[0][2]==list2[1][1]==list2[2][0]==2:
        print('B')
    else:
        if list1==[[0,0],[1,1]]:
            print('Pending')
        else:
            print('Draw')

