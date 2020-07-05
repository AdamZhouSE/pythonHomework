num=int(input())
re=0
if num==1:
    print('False')
else:
    while num>1:
        re=num%3
        num=num/3
        num=int(num)
        if re>0:
           print('False')
           break
    if re==0:
        print('True')