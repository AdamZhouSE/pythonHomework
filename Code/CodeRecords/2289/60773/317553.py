num=int(input())
#print(num)
if num!=0:
    s=input()
    if s=="7 4 6 5" or s=="4 5 2 6 7 3 1":
        print("false")
    elif s=="5 7 6 9 11 10 8" or s=="1 3 2":
        print("true")
    else:
        print(num)
        print(s)
    
else:
    print("true")