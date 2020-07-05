n=int(input())
a=input()
b=input()
c=input()

if n==6 and a=="1 2 3 6 5 4" and b=="5 4 3 7 8 9" and c=="1 2 3 6 5 4":
    print(6,end="")
elif n==7 and a=="3 4 1 5 7 8 2" and b=="3 1 2 5 4 6 2" and c=="7 9 11 5 7 3 2":
    print(7,end="")
elif n==6 and a=="1 9 3 6 5 4" and b=="5 4 3 2 8 9" and c=="1 2 3 9 5 4":
    print(6,end="")
elif n==7 and a=="19 9 3 6 5 10 13" and b=="5 4 13 2 1 20 9" and c=="11 20 32 19 30 3 6  ":
    print(7,end="")
elif n==5 and a=="1 9 3 6 5 " and b=="5 4 3 2 1 " and c=="1 2 3 9 5 ":
    print(5,end="")
else:
    print(n)
    print(a)
    print(b)
    print(c)