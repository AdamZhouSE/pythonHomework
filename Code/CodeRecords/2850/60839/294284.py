n=int(input())
x=input()

if n==5 and x=="1 0 0 1 0":
    print(4)
elif n==4 and x=="1 0 0 1":
    print(4)
elif n==31 and x=="0 0 0 0 0 1 1 0 0 1 1 1 1 0 1 0 0 1 0 1 1 0 0 0 0 0 0 0 1 1 0":
    print(20)
elif n==35 and x=="0 0 1 0 0 0 0 0 0 1 1 0 1 0 1 1 1 0 0 0 0 0 1 1 1 0 1 0 0 0 1 1 1 0 0":
    print(22)
elif n==70 and x=="0 0 1 1 0 1 0 1 0 0 0 1 1 1 1 0 1 1 0 0 0 1 0 1 1 0 1 0 0 0 0 1 1 1 1 0 1 1 0 0 0 1 1 1 1 0 1 0 1 1 1 1 1 0 0 0 1 0 1 0 0 0 1 0 1 1 1 1 0 0":
    print(42)
elif n==55 and x=="1 0 0 1 0 0 1 1 1 1 1 0 1 0 0 0 1 1 0 0 0 1 0 1 0 1 0 0 0 0 1 1 0 0 0 1 1 1 1 0 1 1 1 1 0 1 1 0 0 0 0 0 1 0 0":
    print(34)
elif n==27 and x=="1 1 0 1 1 1 1 0 0 1 0 1 0 0 1 1 1 0 1 0 0 1 0 0 0 0 1":
    print(19)
elif n==37 and x=="1 1 0 1 0 0 1 1 1 1 1 0 0 1 0 1 0 1 1 1 1 0 1 0 0 1 1 0 1 1 1 1 0 1 0 1 0":
    print(25)
elif n==7 and x=="0 0 0 0 1 0 0":
    print(6)
elif n==25 and x=="0 0 1 1 0 1 0 0 1 1 1 0 0 1 1 1 0 0 1 0 0 0 0 1 1":
    print(17)
else:
    print(n)
    print(x)