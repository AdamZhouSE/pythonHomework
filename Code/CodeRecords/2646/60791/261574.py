T = int(input())
x = 0
while(x<T):
    x+=1
    temp = int(input())
    print('Player A') if temp%2==1 else print('Player B')