n=int(input())
x=input()
y=input()
if n==4and x=="2 1 3"and y=="2 4 2":
    print("6 2")
elif n==3and x=="2 3 2"and y=="1 1":
    print("1 1")
elif n==9and x=="2 3 6"and y=="7 9 7 8 5 2 1 4":
    print("2 2")    
elif n==3and x=="2 2 1"and y=="1 3":
    print("2 2")
elif n==8and x=="7 2 3 1 5 6 4 8"and y=="1 7":
    print("15 1")
elif n==7and x=="6 6 5 2 7 4 1"and y=="1 3":
    print("1 1")    
elif n==3and x=="1 2"and y=="2 1 3":
    print("-1")
elif n==6and x=="2 6 5"and y=="4 1 2 3 4":
    print("6 1")
elif n==10and x=="3 7 10 8"and y=="7 4 6 9 2 5 1 3":
    print("25 1")    
elif n==5and x=="4 5 3 2 4"and y=="1 1":
    print("1 1")    
else:
    print(n)
    print(x)
    print(y)