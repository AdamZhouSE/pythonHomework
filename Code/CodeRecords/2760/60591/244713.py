n = eval(input())
while(n != 0):
    n = n - 1
    N,money = list(map(int,input().split(" ")))
    if(N % 2 == 1):
        print(money * (int(N/2) + 1))
    else:
        print(money * int(N/2))