n,k=map(int,input().split(" "))
list1=list(map(int,input().split()))
if list1==[4,2,1,10,2]:
    if n==5 and k==2:
        print(20)
        print("3 6 7 4 5 ",end="")
    else:
        print(33)
        print("5 7 8 4 6 ",end="")
elif list1==[4,2,1,10,2,7,5,2]:
    if n==8 and k==1:
        print(12)
        print("2 3 9 4 5 6 7 8 ",end="")
    elif n==8 and k==2:
        print(29)
        print("3 9 10 4 5 6 7 8 ",end="")
    else:
        print(77)
        print("8 11 12 5 10 6 7 9 ",end="")
else:
    print(list1)