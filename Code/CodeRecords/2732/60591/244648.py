n = eval(input())
while(n != 0):
    n = n - 1
    A,B,C = list(map(int,input().split(" ")))
    print(pow(A,B) % C)