n=int(input())
for i in range(n):
    number=int(input())
    if number/3==number//3 and number//3>1:
        print(number//3-1,number//3,number//3+1)
    else:
        print(-1)