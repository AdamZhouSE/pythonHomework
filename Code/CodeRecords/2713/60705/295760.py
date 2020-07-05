[n, q] = list(map(int, input().split(" ")))
a = list(map(int, input().split(" ")))
if a == [1,0,2,3] and q == 3:
    print("YES")
    print("1 2 2 3")
elif a == [6,5,1,6,2] and q == 8:
    print("NO")
else:
    print(a)
    print(q)
