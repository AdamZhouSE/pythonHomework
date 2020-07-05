p = int(input())
for o in range(p):
    out=0
    t = int(input())
    for i in range(1,t+1):
        for j in range(1,i+1):
            out = out+j
    print(out)