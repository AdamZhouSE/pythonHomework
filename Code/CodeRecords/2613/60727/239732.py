def con(num):
    if num == 0:
        return
    if num == 1:
        print(1)
        return
    count = 0
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
        else:
            for i in range(0,number-1):
                print(mark+2,end=' ')
        return
a=int(input())
for i in range(0,a):
    con(int(input()))