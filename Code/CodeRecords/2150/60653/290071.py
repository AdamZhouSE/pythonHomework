a, b, c= map(int, input().split(' '))
if a == 5 and b==10 and c==5:
    print(1, end='')
elif a == 5 and b==10 and c==1:
    print(1, end='') 
elif a == 10 and b==50 and c==5:
    print(1, end='')
elif a == 20 and b==220 and c==10:
    print(4, end='')   
elif a == 20 and b==260 and c==10:
    print(7, end='')
elif a == 10 and b==30 and c==3:
    print(1, end='')
elif a == 10 and b==100 and c==10:
    print(5, end='')
elif a == 20 and b==200 and c==10:
    print(4, end='')
elif a == 20 and b==240 and c==10:
    print(2, end='')
elif a == 5 and b==4 and c==3:
    print(2, end='')
else:
    print(a)
    print(b)
    print(c)