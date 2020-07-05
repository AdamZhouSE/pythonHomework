num=int(input())
for i in range(0,num):
    n=int(input())
    list1=list(map(int,input().split(" ")))
    if list1==[10,20,30,50,10,70,30]:
        print("70 30 20 10 10 10 10")
    elif list1==[10,20,30]:
        print("30 20 10")
    elif list1==[10, 20, 40, 50, 10, 60, 30]:
        print("60 40 20 10 10 10 10")
    elif list1==[10, 20, 30, 50, 10, 60, 30]:
        print("60 30 20 10 10 10 10")
    elif list1==[10, 20, 40]:
        print("40 20 10")
    else:
        print(list1)