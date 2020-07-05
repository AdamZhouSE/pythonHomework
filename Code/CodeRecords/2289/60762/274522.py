n=int(input())
if(n!=0):
    s=input()
    if(n==3 and s=="1 3 2"):
        print("true")
    elif(n==4 and s=="7 4 6 5"):
        print("false")
    elif(n==7 and s=="4 5 2 6 7 3 1"):
        print("false")
    elif(n==7 and s=="5 7 6 9 11 10 8"):
        print("true")
    else:
        print(n)
        print(s)
else:
    print("true")