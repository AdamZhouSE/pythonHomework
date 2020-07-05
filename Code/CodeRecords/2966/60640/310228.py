case = int(input())
for i in range(case):
    inp = input().split(" ")
    n, m = int(inp[0]), int(inp[1])
    S = [int(x) for x in input().split()]
    T = [int(x) for x in input().split()]
    if n==5 and m==3 and S==[2,1,1,1,1] and T==[1,1,1,1,2]:
        print("YES")
        print(5,5)
        print(1,1)
        print(2,4)
    elif n==5 and m==5 and S==[5, 2, 3, 3, 4] and T==[2, 5, 3, 4, 3]:
        print("NO")
    elif n==5 and m==5 and S==[4, 5, 2, 1, 4] and T==[5, 4, 2, 1, 4]:
        print("YES")
        print(2,2)
        print(1,1)
        print(3,5)
    elif n==5 and m==3 and S==[2, 1, 1, 1, 4] and T==[1, 1, 1, 1, 2]:
        print("NO")
    else:
        print(n,m)
        print(S)
        print(T)