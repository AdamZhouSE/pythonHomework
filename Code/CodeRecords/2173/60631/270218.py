p = int(input())
for o in range(p):
    out=0
    t = int(input())*2-1
    for i in range(1,t+1):
        if i%2!=0:
            for j in range(1,i+1):
                if j%2!=0:
                    out = out+j
    print(out)