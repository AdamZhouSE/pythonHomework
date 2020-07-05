t=int(input())
for i in range(t):
    n=int(input())
    for j in range(32):
        if n<1<<j:
            print((1<<j)-1-n)
            break