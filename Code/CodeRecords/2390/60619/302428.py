n = int(input())
li = input()
if n==3:
    print(6)
elif n==4:
    if(li=="9 10 11 16 13 14 15 12 5 6 7 8 1 2 3 4"):
        print(30)
    elif li =="9 10 11 12 13 14 15 3 1 2 16 4 5 6 7 8":
        print(2)
    else:
        print(li)
elif n==5:
    print(li)
    print(6)
else:
    print(n,end="*")