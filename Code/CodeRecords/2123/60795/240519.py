num=int(input())
com,mark=0,0
for i in range(1,num):
    com=i*i
    if com==num:
        mark=1
        break
    elif com>num:
        break
if mark==1:
    print('True')
else:
    print('False')