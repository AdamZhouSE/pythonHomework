T=int(input())
for i in range(T):
    s=input()
    sets=set(s)
    lens=len(sets)
    tem={'a','e','u','i','o'}
    for i in tem:
        if i in sets:
            lens-=1
    if lens%2==0:
        print("SHE!")
    else:
        print("HE!")