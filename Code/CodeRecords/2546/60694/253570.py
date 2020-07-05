def Padovan(x):
    if x == 0 or x == 1 or x == 2:
        return 1
    else:
        return Padovan(x-2) + Padovan(x-3)


T = int(input())
for i in range(T):
    N = int(input())
    print(Padovan(N))
