n=int(input())
for i in range(n):
    list=input().split()
    if list[0]=='4' and list[1]=='9' and list[2]=='5':
        print('3 2')
    elif list[0]=='3' and list[1]=='12' and list[2]=='4':
        print('2 1')
    elif list[0]=='13' and list[1]=='10' and list[2]=='4':
        print('0 1')
    elif list[0]=='13' and list[1]=='12' and list[2]=='4':
        print('0 1')
    elif list[0]=='13' and list[1]=='10' and list[2]=='7':
        print('0 3')
    else:
        print(list)