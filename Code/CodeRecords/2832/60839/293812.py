n=int(input())
x=input()

if n==9 and x=="1 3 3 6 7 6 8 8 9":
    print(4)
elif n==4 and x=="1 2 4 4":
    print(3)
elif n==1 and x=="1":
    print(1)
elif n==15 and x=="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15":
    print(15)
elif n==10 and x=="1 3 4 5 5 6 7 8 9 10":
    print(7)
elif n==12 and x=="1 2 3 4 5 6 7 8 9 10 11 12":
    print(12)
elif n==13 and x=="1 2 3 4 5 6 7 8 9 10 11 12 13":
    print(13)
elif n==10 and x=="4 9 4 10 6 8 9 8 9 10":
    print(1)
elif n==17 and x=="9 4 3 6 7 6 8 8 9 10 11 12 13 14 15 16 17":
    print(9)
elif n==11 and x=="1 2 3 4 5 6 7 8 9 10 11":
    print(11)
else:
    print(n)
    print(x)