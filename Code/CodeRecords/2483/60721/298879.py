T=int(input())
for i in range(0,T):
    s=list(input())
    p=list(input())
    q=False
    for j in s:
        if(j in p):
            print(j)
            q=True
            break
    if(q==False):
        print("$")