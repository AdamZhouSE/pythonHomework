n = eval(input())
while(n!=0):
    n = n - 1
    m = eval(input())
    if(m == 2 or m == 4 or m == 14 or m == 12):
        print(1)
    elif(m == 1 or m == 121 or m == 141):
        print(0)
    else:
        print("_"+str(m))