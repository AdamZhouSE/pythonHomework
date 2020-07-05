def tb13():
    n=int(input())
    for i in range(n):
        strs=input().split(' ')
        num1,num2=int("0b"+strs[0],2),int("0b"+strs[1],2)
        print(num1*num2)
    return 

tb13()