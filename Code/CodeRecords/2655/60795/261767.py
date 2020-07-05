T=int(input())
for i in range(0,T):
    num=int(input())
    k=0
    two=1
    while True:
        if num>two:
            k=k+1
            two=two*2
        else:
            break
    print(two)
