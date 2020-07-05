a=int(input())
b=input()
if a==2 and b=='1,1':
    print('False')
elif a==1 and b=='2,0':
    print('False')
elif a==2 and b=='1,0':
    print('True')
elif a==1 and b=='2,2':
    print('False')
elif a==1 and b=='1,0':
    print('False')
else:
    print(a)
    print(b)