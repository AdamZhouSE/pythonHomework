n = eval(input())
if(n % 2 == 0):
    print(-1)
else:
    situation = True
    for x in range(1,n*10 + 1):
        if(eval('1' * x) % n == 0):
            situation = False
            print(x)
            break
    if(situation):
        print(-1)