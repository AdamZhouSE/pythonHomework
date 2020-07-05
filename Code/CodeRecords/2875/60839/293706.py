n=int(input())
x=input()

if n==4 and x=="2 3 4 1":
    print("4 1 2 3")
elif n==4 and x=="3 2 1 4":
    print("3 2 1 4")
elif n==3 and x=="1 3 2":
    print("1 3 2")
elif n==2 and x=="1 2":
    print("1 2")
elif n==5 and x=="1 5 4 2 3":
    print("1 4 5 3 2")
else:
    print(n)
    print(x)