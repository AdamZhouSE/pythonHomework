for t in range(int(input())):
    n = int(input())
    n2 = n+2
    for i in range(2,n2):
        if n2%i==0:
            print("No")
            break
    else:
        print("Yes")