n = int(input())
while(n>0):
    m = int(input())+1
    out = 0
    for i in range(1,m):
        out = out+ i*(i+1)/2
    out = int(out)
    print(out)
    n-=1