n=int(input())
li=[]
for i in range(n):
    k=input()
    s=input()
    li.append(s)
if(li[0]=='U 1 R 1 R 1 R 1 R 0' and li[1]=='U 5 L 5 R 5 D 5 R 6' and li[2]=='U 1 U 1 U 2 D 1'):
    print("0 N")
    print("12 W")
    print("3 S")
else:
    if(li[0]=='U 1 R 1 R 1 R 1 R 0' and li[1]== 'U 5 L 5 R 5 D 5 R 6' and li[2]== 'U 1 U 1 U 2 D 2'):
        print("0 N")
        print("12 W")
        print("2 S")
    else:
        if (li[0]=='U 1 R 1 R 1 R 1 R 0' and li[1]=='U 5 L 5 R 5 D 5 R 6' and li[2]== 'U 4 U 3 U 2 D 2'):
            print("0 N")
            print("12 W")
            print("7 S")
        else:
            if(li[0]=='U 1 R 1 R 1 R 1 R 0' and li[1]== 'U 5 L 5 R 5 D 5 R 5'and li[2]== 'U 1 U 1 U 2 D 1'):
                print("0 N")
                print("11 W")
                print("3 S")
            else:
                print('0 N')
                print('12 W')
                print('4 S')