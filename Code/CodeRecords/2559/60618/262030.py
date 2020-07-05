t=int(input())
for i in range(0,t):
    test=list(input())
    if len(test)!=len(set(test)):
        print(0)
    else:
        print(1)