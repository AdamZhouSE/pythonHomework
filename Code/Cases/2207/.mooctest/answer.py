for i in range(int(input())):
    num1,num2=map(int,input().split())
    p=(num2*(num2+1))//2
    if num1>=p:
        print(1)
    else:
        print(0)