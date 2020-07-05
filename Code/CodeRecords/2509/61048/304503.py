def tree3():
    num=int(input())
    set=[]
    for x in input().split(' '):
        set.append(int(x))
    order_no=int(input())
    for i in range(order_no):
        str=input()
        if(str=='mid'):
            print(set[(len(set)-1)//2])
        else:
            set.append(int(str.split(' ')[1]))
            set.sort()
    return

tree3()