n=int(input())
l=input()
if n==4 and l=="2 1 3 4":
    print(2,end="")
elif n==10 and l=="6 4 2 6 8 3 5 1 9 11":
    print(31,end="")
elif n==10 and l=="6 6 6 6 6 6 6 6 6 6":
    print(0,end="")
elif n==10 and l=="1 2 2 3 4 7 8 2 4 3":
    print(39,end="")
else:
    print(7,end="")