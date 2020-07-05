m,n = list(map(int,input().split(" ")))
a = list(map(int,input().split(" ")))
while(n != 0):
    n -= 1
    string = input().strip()
    op = list(map(int,string.split(" ")))
    if(op[0] == 1):
        L,R,K,D = op[1:]
        for x in range(L - 1,R):
            a[x] += K + (x + 1 - L) * D
    elif(op[0] == 2):
        P = op[1]
        print(a[P - 1])