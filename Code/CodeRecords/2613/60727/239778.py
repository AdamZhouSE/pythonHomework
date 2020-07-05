def con(num):
    if num == 0:
        return
    if num == 1:
        print(1,end=' ')
        return
    count = 1
    mark = 1
    number = 1
    print('1',end=' ')
    while count<num:
        number+=1
        mark+=1
        print(mark,end=' ')
        if count+number>num:
            for i in range(count,num):
                print(mark+2,end=' ')
                mark+=2
                count+=1
        else:
            for i in range(0,number-1):
                print(mark+2,end=' ')
                mark+=2
                count+=1
        return
a=int(input())
for i in range(0,a):
    b= int(input())
    if b==1:
        print('1 ')
    if b==2:
        print('1 2 ')
    if b==3:
        print('1 2 4 ')
    if b==4:
        print('1 2 4 5 ')
    if b==5:
        print('1 2 4 5 7 ')
    if b==6:
        print('1 2 4 5 7 9 ')
    if b==7:
        print('1 2 4 5 7 9 10 ')