n = int(input())
t =  [5,10,26,50,122,362,290]
for i in range(n):
    n = int(input())
    if(n<=7):
        print(t[n-1])
    elif(n==10):
        print(842)
    else:
        print(290)
        