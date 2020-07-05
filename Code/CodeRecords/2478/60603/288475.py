testnum=int(input())
for i in range(testnum):
    string=input().split(" ")
    num1=int(string[0])
    num2=int(string[1])
    list=[]
    list.append(num1)
    list.append(num2)
    order=int(input())
    if(order<=2):
        print(list[order-1])
    else:
        d=num2-num1
        for i in range(order):
            list.append(list[-1]+d)
        print(list[order-1])