T=int(input())
for i in range(T):
    s=input()
    sSet=set(s)
    if len(s)==len(sSet):
        print(1)
    else:
        print(0)