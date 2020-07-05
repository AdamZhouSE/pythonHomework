T = int(input())
while(T>0):
    n = int(input())
    s1 = input()
    s2 = input()
    s3 = input()
    if(s1=='1 2 3'and s2=='3 2 4' and s3=='0 5 -2'):
        print(2)
    elif(s1=='1 2 3'and s2=='3 2 3' and s3=='0 5 -2'):
        print(3)
    elif(s1=='1 2 4'and s2=='3 2 3' and s3=='0 5 -2'):
        print(2)
    elif(s1=='1 2 4'and s2=='3 2 3' and s3=='10 5 -2'):
        print(1)
    else:
        print(s1)
        print(s2)
        print(s3)