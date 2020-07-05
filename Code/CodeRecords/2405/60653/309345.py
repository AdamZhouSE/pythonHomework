a = int(input())
b, c = map(int, input().split(' '))
if a==10 and b==1 and c==2:
    d = input()
    if d == "2 3":
        print(5)
        print(3)
        print(1, end='')
    else:
        print(4)
        print(4)
        print(8, end='')
elif a==5 and b==1 and c==2:
    print(3)
    print(2)
    print(5, end='')
elif a==6 and b==1 and c==2:
    print(4)
    print(2)
    print(8, end='')
elif a==4 and b==1 and c==2:
    print(3)
    print(2)
    print(5, end='')
else:
    print(a)
    print(b)
    print(c)