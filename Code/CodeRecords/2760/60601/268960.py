n = eval(input())
for i in range(n):
    line = input().split(' ')
    N = int(line[0])
    money = int(line[1])
    if N%2!=0:
        N = N//2+1
    else:
        N = N//2
    print(N*money)