num=int(input())
re=0
mark=0
if num==1:
    print('True')
else:
    while num>1:
        re = num % 2
        num=num/2
        if re>0:
            print('False')
            mark=1
            break
    if mark==0:
        print('True')