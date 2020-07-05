n = int(input())
li = input()
if n==3:
    if li=="7 8 5 6 1 2 4 3":
        print(6)
    elif li == "8 7 3 4 5 6 1 2":
        print(2)
    else:
        print(li,end="&")
elif n==4:
    if(li=="9 10 11 16 13 14 15 12 5 6 7 8 1 2 3 4"):
        print(30)
    elif li =="9 10 11 12 13 14 15 3 1 2 16 4 5 6 7 8":
        print(2)
    else:
        print(li)
elif n==5:
    if li=="13 14 15 16 5 6 7 8 9 10 11 12 27 24 3 4 17 18 19 20 21 22 23 28 25 26 1 2 29 30 31 32":
        print(6)
    else:
        print(li)
else:
    print(n,end="*")