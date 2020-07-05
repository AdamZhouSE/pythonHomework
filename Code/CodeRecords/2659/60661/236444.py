t=int(input())
for i in range(t):
    xg=input()
    x = int(xg.split(' ')[0])
    g = int(xg.split(' ')[1])
    print(~(x - g))