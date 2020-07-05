

T = int(input())
x = 0
while(x < T):
    x += 1
    a,b = [int(i) for i in input().split(' ')]
    print(int(a/2)*2*b)